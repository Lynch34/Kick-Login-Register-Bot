from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from colorama import Fore, Style
from seleniumbase import Driver
from time import sleep
import random
import string
import re

def human_delay(min=1, max=3):
    sleep(random.uniform(min, max))

def human_type(element, text, delay_range=(0.1, 0.3)):
    for char in text:
        element.send_keys(char)
        sleep(random.uniform(*delay_range))

def slow_scroll(driver, element, scroll_step=1500, delay_range=(0.1, 0.2)):
    current_scroll = 0
    total_height = driver.execute_script("return arguments[0].scrollHeight", element)
    
    while current_scroll < total_height + 1500:
        driver.execute_script(f"arguments[0].scrollTop = {current_scroll}", element)
        current_scroll += scroll_step
        sleep(random.uniform(*delay_range))

def save_account_to_file(email, username, password, filename="accounts.txt"):
    with open(filename, "a") as file:
        file.write(f"Email: {email} | Username: {username} | Password: {password}\n")
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Account saved.")

def generate_username():
    syllables = [
        "al", "ar", "er", "il", "in", "an", "em", "el", "en", "on", "ur", "um", 
        "at", "as", "es", "is", "os", "us", "ik", "ok", "ak", "et", "uz", "ot", "im", "ul"
    ]
    letters = string.ascii_letters
    digits = string.digits

    nickname = ''.join(random.choices(syllables, k=random.randint(2, 4)))
    nickname = nickname[:1].upper() + nickname[1:]
    nickname = ''.join(
        char.upper() if random.choice([True, False]) else char
        for char in nickname
    )

    if random.choice([True, False]):
        random_number = ''.join(random.choices(digits, k=random.randint(1, 3)))
        insert_position = random.randint(0, len(nickname))
        nickname = nickname[:insert_position] + random_number + nickname[insert_position:]

    while len(nickname) < random.randint(7, 12):
        nickname += random.choice(letters)

    nickname = ''.join(random.sample(nickname, len(nickname)))

    print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Generated nick: {nickname}.")
    return nickname

def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    password_letters = ''.join(random.choices(letters, k=8))
    password_digits = ''.join(random.choices(digits, k=3))
    password = password_letters + password_digits + '@'
    password = ''.join(random.sample(password, len(password)))
    
    print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Genetared pass: {password}.")
    return password

def generate_birthdate():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1980, 2005)
    return f"{day:02d}.{month:02d}.{year}"

def get_random_email():
    mail_driver = Driver(uc=True, chromium_arg="--mute-audio")
    url = "https://emailfake.com/sunstorevn.com" # You can customize domain, i prefer sunstorevn.
    mail_driver.maximize_window()
    mail_driver.get(url)
    mail_driver.implicitly_wait(10)

    username_element = mail_driver.find_element(By.ID, "userName")
    username = username_element.get_attribute("value").strip()

    domain_element = mail_driver.find_element(By.ID, "domainName2")
    domain = domain_element.get_attribute("value").strip()

    email_address = f"{username}@{domain}"

    print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Email address: {email_address}.")
    return mail_driver, email_address

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

def register_kick():
    mail_driver = None
    driver_kick = None
    try:
        username = generate_username()
        password = generate_password()
        birthdate = generate_birthdate()
        mail_driver, email_address = get_random_email()

        driver_kick = Driver(uc=True, chromium_arg="--mute-audio")
        url = "https://kick.com/"
        driver_kick.maximize_window()
        driver_kick.get(url)
        driver_kick.implicitly_wait(10)

        register_button = WebDriverWait(driver_kick, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/nav/div[3]/button[2]'))
        )
        ActionChains(driver_kick).move_to_element(register_button).click().perform()
        human_delay(1, 2)

        email_input = driver_kick.find_element(By.XPATH, "//input[@placeholder='you@example.com']")
        human_type(email_input, email_address)

        birthdate_input = driver_kick.find_element(By.CSS_SELECTOR, "input[name='birthdate']").send_keys(birthdate)

        username_input = driver_kick.find_element(By.CSS_SELECTOR, "input[name='username']")
        human_type(username_input, username)

        password_input = driver_kick.find_element(By.CSS_SELECTOR, "input[name='password']")
        human_type(password_input, password)

        submit_button = WebDriverWait(driver_kick, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/form/button'))
        )
        submit_button.click()

        verification_code = check_email(mail_driver)
        if verification_code is None:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Failed to receive verification code. Drivers will shut down.")
            driver_kick.quit()
            mail_driver.quit()
            return

        code_input = WebDriverWait(driver_kick, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='code']"))
        )
        human_type(code_input, verification_code)
        human_delay(2, 3)

        scroll_area = driver_kick.find_element(By.CSS_SELECTOR, '[data-radix-scroll-area-viewport]')
        slow_scroll(driver_kick, scroll_area)

        final_button = WebDriverWait(driver_kick, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/form/button"))
        )
        final_button.click()
        human_delay(4, 5)

        confirm_button = WebDriverWait(driver_kick, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[2]/button"))
        )
        confirm_button.click()
        human_delay(2, 3)

        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Account created successfully.")
        save_account_to_file(email_address, username, password)

    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}[!] {Style.RESET_ALL}Register error: {e}")
    finally:
        if driver_kick:
            driver_kick.quit()
        if mail_driver:
            mail_driver.quit()

def main():
    while True:
        try:
            register_kick()
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Error: {e}")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Script ended.")