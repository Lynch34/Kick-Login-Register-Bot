from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore, Style
from seleniumbase import Driver
from time import sleep
import re

global accountId

channel_url = input("Target Kick Name: ")
accountId = int(input("Input Account Id: "))
message_mode = int(input("Message Mod (0- Off | 1- Constant Message | 2- Static Message): "))

if(message_mode == 1):
    const_message = input("Input Message: ")

def get_account(iNumber):
    accounts = []

    with open("accounts.txt", "r") as file:
        data = file.readlines()

    for line in data:
        match = re.match(r"Email:\s*(\S+)\s*\|\s*Username:\s*(\S+)\s*\|\s*Password:\s*(\S+)", line)
        if match:
            email, username, password = match.groups()
            accounts.append({
                "email": email,
                "username": username,
                "password": password
            })

    email_adress = accounts[iNumber]['email']
    username = accounts[iNumber]['username']
    password = accounts[iNumber]['password']

    return email_adress, username, password

def get_email():
    mail_driver = Driver(
        uc=True,
        chromium_arg="--mute-audio",
        block_images=True,
        ad_block=True
    )
    url = "https://emailfake.com/"
    mail_driver.maximize_window()
    mail_driver.get(url)
    mail_driver.implicitly_wait(10)

    email_adress, _, _ = get_account(accountId)

    username_input = mail_driver.find_element(By.ID, "userName")
    username_input.clear()
    username_input.send_keys(email_adress.split('@')[0])
    
    sleep(1)
    
    domain_input = mail_driver.find_element(By.ID, "domainName2")
    domain_input.click()
    domain_input.send_keys(Keys.CONTROL + "a")
    domain_input.send_keys(Keys.DELETE)
    domain_input.send_keys(email_adress.split('@')[1])
    
    mail_driver.find_element(By.ID, "refresh").click()

    print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Email address: {email_adress}.")
    return mail_driver

def check_email(mail_driver, max_retries=5):
    mail_driver.refresh()
    
    verification_code = None
    retry_count = 0
    while retry_count < max_retries:
        try:
            code_elements = mail_driver.find_elements(By.CSS_SELECTOR, ".e7m.subj_div_45g45gg")
            
            if code_elements:
                for code_element in code_elements:
                    code_text = code_element.text
                    
                    match = re.search(r'\d{6}', code_text)
                    if match:
                        verification_code = match.group(0)
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Verification code: {verification_code}.")
                        return verification_code
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Verification code not found, trying again.")
                retry_count += 1
            
        except Exception as e:
            retry_count += 1
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Error: {e}. Verification code not found, checking again... ({retry_count}/{max_retries})")
            sleep(5)
    
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Verification code not found, cancelled.")
    return None

def login_kick():
    global accountId

    while True:
        try:
            _, username, password = get_account(accountId)

            driver_kick = Driver(
                uc=True,
                chromium_arg="--mute-audio",
                block_images=True,
                ad_block=True
            )
            driver_kick.maximize_window()
            driver_kick.open(f"https://kick.com/{channel_url}")
            driver_kick.implicitly_wait(10)

            login_button = WebDriverWait(driver_kick, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/nav/div[3]/button[1]'))
            )
            login_button.click()
            
            sleep(1)

            driver_kick.find_element(By.CSS_SELECTOR, "input[name='emailOrUsername']").send_keys(username)
            driver_kick.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
            driver_kick.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/form/button').click()

            mail_driver = get_email()
            verification_code = check_email(mail_driver)

            if verification_code is None:
                raise Exception("Verification code not found.")

            verification_input = WebDriverWait(driver_kick, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='code']"))
            )
            verification_input.send_keys(verification_code)
            
            sleep(2)

            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}{username} login successfully.")
            
            accountId += 1
            
            # Çerez Kabul
            try:
                accept_button = WebDriverWait(driver_kick, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Kabul Et']"))
                )
                accept_button.click()
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}{username} accepted cookies.")
            except Exception:
                print(f"{Fore.LIGHTYELLOW_EX}[+] {Style.RESET_ALL}{username} cannot accepted cookies.")
            
            sleep(1)
            
            # Takip Et
            try:
                follow_button = WebDriverWait(driver_kick, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Takip Et']"))
                )
                follow_button.click()
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}{username} followed successfully.")
            except Exception:
                print(f"{Fore.LIGHTYELLOW_EX}[!] {Style.RESET_ALL}{username} follow error.")
            
            sleep(2)
            
            # Mesaj
            if(message_mode != 0):
                # Chat Kural
                try:
                    message_button = WebDriverWait(driver_kick, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[text()='Kabul ediyorum']"))
                    )
                    message_button.click()
                    print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}{username} chat rules accepted successfully.")
                except Exception:
                    print(f"{Fore.LIGHTYELLOW_EX}[!] {Style.RESET_ALL}{username} chat rules not accepted.")
                
                try:
                    message_input = WebDriverWait(driver_kick, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "div.editor-input[data-input='true']"))
                    )
                    
                    if(message_mode == 2):
                        user_message = input("Mesaj giriniz: ")
                        message_input.send_keys(user_message)
                    elif(message_mode == 1):
                        message_input.send_keys(const_message)

                    send_button = WebDriverWait(driver_kick, 10).until(
                        EC.element_to_be_clickable((By.ID, 'send-message-button'))
                    )
                    send_button.click()
                    print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}{username} message send successfully.")
                except Exception:
                    print(f"{Fore.LIGHTYELLOW_EX}[!] {Style.RESET_ALL}{username} message not send.")

            break

        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Login error: {e}")

        finally:
            try:
                mail_driver.quit()
            except:
                pass
            try:
                driver_kick.quit()
            except:
                pass

def main():
    while True:
        try:
            login_kick()
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Error: {e}")
            break
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Script ended.")