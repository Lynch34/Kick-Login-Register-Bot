## Türkçe

# Proje

Yapımcı: [LyNcH](https://github.com/Lynch34)  
Link: [https://github.com/Lynch34/Kick-Login-Register-Bot](https://github.com/Lynch34/Kick-Login-Register-Bot)

# Bilgilendirme

- Bu script eğitim amaçlı yapılmıştır.
- Belli bir kullanımdan sonra geçici ip ban yiyebilirsiniz, tüm sorumluluk kullanıcıya aittir.
- Proxy kullanmanız oluşan hataları minimuma indirecektir.

# Kick Hesap Oluşturma ve Giriş Scripti
  
- Bu Python scripti, Selenium kullanarak Kick sitesinde otomatik olarak hesap oluşturma ve hesaba giriş yapma işlemlerini gerçekleştirir.
- Hesaba giriş yaptırdıktan sonra, takip ettirme ve mesaj attırma özelliği bulunmaktadır.

## Özellikler

1. **Hesap Oluşturma:**
   - Scripti çalıştırmanız yeterlidir, ayar yapmanıza gerek yok.
   - Kick sitesinde yeni bir hesap oluşturur.
   - Mail doğrulamasını emailfake.com üzerinden yapar ve hesabı bir dosyaya kayıt eder.
   - Rastgele kullanıcı adı ve şifre üretir.
   - Headless açmanız önerilmez.
     
2. **Otomatik Giriş:**
   - Kaydedilen hesap bilgileriyle otomatik giriş yapar.
   - Belirlediğiniz kullanıcıya takip, mesaj atabilirsiniz.
   - Hesaplara tek tek girerek işlemleri sırayla yapar.

## Gereksinimler

- Python 3.13.0
- Seleniumbase kütüphanesi (`pip install seleniumbase`)
- Colorama kütüphanesi (`pip install colorama`)
- ChromeDriver (Selenium ile otomatik yüklenir)

## Kurulum

1. **Python'u yükleyin:**
   - [Python resmi sitesinden](https://www.python.org/downloads/) Python'u indirip yükleyin.

2. **Gerekli paketleri yükleyin:**
   - Terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:
     ```bash
     pip install seleniumbase colorama
     ```

4. **Script'i indirin:**
   - Bu depoyu klonlayın veya script dosyasını manuel indirin:
     ```bash
     git clone https://github.com/Lynch34/Kick-Login-Register-Bot.git
     ```

## Kullanım

1. **Kayıt**
   - Terminal veya komut istemcisinde script'in bulunduğu dizine gidin ve aşağıdaki komutu çalıştırın:
     ```bash
     python kick-register.py
     ```

     Kod döngü şeklinde hesap üretmeye başlayacaktır.

2. **Giriş**
   - Terminal veya komut istemcisinde script'in bulunduğu dizine gidin ve aşağıdaki komutu çalıştırın:
     ```bash
     python kick-login.py
     ```

   - "Target kick name" input alanına takip ve mesaj göndermek istediğiniz kullanıcı adını girin.
   - "Account Id" input alanına hesap idsi giriniz, dosyada kaçıncı hesaptan başlamasını istiyorsanız ona girin, başlangıç 0.
   - "Message Mod" input alanına (0, 1, 2) giririniz:
     - `0`: Mesaj atmaz.
     - `1`: Hep aynı mesajı atar (mesajı siz belirlersiniz).
     - `2`: Her mesaj atılmadan önce siz belirleyeceksiniz.

   - Script, Kick sitesinde hesap oluşturma ve giriş işlemlerini otomatik olarak gerçekleştirecektir.

## Örnek Çıktı

Kayıt scripti başarıyla çalıştığında aşağıdaki gibi bir çıktı göreceksiniz:
```[+] Generated nick: rtUstaAsEs.
[+] Genetared pass: iJC02r8PtJI@.
[+] Email address: xxx@xxx.com.
[+] Verification code: xxxxxx.
[+] Account created successfully.
[+] Account saved.
```

Login scripti başarıyla çalıştığında aşağıdaki gibi bir çıktı göreceksiniz:
```Target Kick Name: random-person
Input Account Id: 0
Message Mod (0- Off | 1- Constant Message | 2- Static Message): 1
Input Message: Hello!
[+] Email address: xxx@xxx.com.
[+] Verification code: xxxxxx.
[+] snYIOEkI login successfully.
[+] snYIOEkI accepted cookies.
[+] snYIOEkI followed successfully.
[!] snYIOEkI chat rules not accepted.
[+] snYIOEkI message send successfully.
```

## English

# Project

Author: [LyNcH](https://github.com/Lynch34)  
Link: [https://github.com/Lynch34/Kick-Login-Register-Bot](https://github.com/Lynch34/Kick-Login-Register-Bot)

# Kick Account Creation and Login Script

This Python script automates the process of creating accounts and logging into the Kick platform using Selenium. After logging in, it can also follow users and send messages.

## Features

1. **Account Creation:**
   - Simply run the script; no additional setup is required.
   - Creates a new account on Kick.
   - Verifies the email using `emailfake.com` and saves the account details to a file.
   - Generates random usernames and passwords.
   - Running in headless mode is not recommended.

2. **Automatic Login:**
   - Logs in automatically using saved account credentials.
   - Can follow and send messages to a specified user.
   - Processes accounts one by one in sequence.

## Requirements

- Python 3.13.0
- Seleniumbase library (`pip install seleniumbase`)
- Colorama library (`pip install colorama`)
- ChromeDriver (automatically installed with Selenium)

## Installation

1. **Install Python:**
   - Download and install Python from the [official Python website](https://www.python.org/downloads/).

2. **Install Required Packages:**
   - Run the following command in your terminal or command prompt:
     ```bash
     pip install seleniumbase colorama
     ```

3. **Download the Script:**
   - Clone this repository or manually download the script files:
     ```bash
     git clone https://github.com/Lynch34/Kick-Login-Register-Bot.git
     ```

## Usage

1. **Registration:**
   - Navigate to the directory containing the script and run the following command:
     ```bash
     python kick-register.py
     ```

   - The script will start creating accounts in a loop.

2. **Login:**
   - Navigate to the directory containing the script and run the following command:
     ```bash
     python kick-login.py
     ```

   - Enter the target Kick username in the "Target kick name" input field.
   - Enter the account ID in the "Account Id" input field (starting from 0).
   - Choose the message mode in the "Message mod" input field:
     - `0`: No messages will be sent.
     - `1`: Sends the same message every time (you will be prompted to enter the message).
     - `2`: Asks for a message before each send.

   - The script will automatically log in and perform the specified actions.

## Example Output

For the registration script, you will see output similar to this:
```[+] Generated nick: rtUstaAsEs.
[+] Genetared pass: iJC02r8PtJI@.
[+] Email address: xxx@xxx.com.
[+] Verification code: xxxxxx.
[+] Account created successfully.
[+] Account saved.
```

For the login script, you will see output similar to this:
```Target Kick Name: random-person
Input Account Id: 0
Message Mod (0- Off | 1- Constant Message | 2- Static Message): 1
Input Message: Hello!
[+] Email address: xxx@xxx.com.
[+] Verification code: xxxxxx.
[+] snYIOEkI login successfully.
[+] snYIOEkI accepted cookies.
[+] snYIOEkI followed successfully.
[!] snYIOEkI chat rules not accepted.
[+] snYIOEkI message send successfully.
```