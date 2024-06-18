import os
import json
import random
from time import sleep as w

def delete_account(username):
    with open('accounts.json', 'r') as f:
        accounts = json.load(f)

    for account in accounts:
        if account['username'] == username:
            accounts.remove(account)
            break
    
    with open('accounts.json', 'w') as f:
        json.dump(accounts, f, indent=4)

def file_exists(file_path):
    return os.path.exists(file_path)

def create_account(username, password):
    if not file_exists("accounts.json"):
        accounts = []
    else:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)

    for account in accounts:
        if account["username"] == username:
            print("Ошибка 1: Аккаунт с таким именем пользователя уже существует.")
            return

    new_account = {"username": username, "password": password}
    accounts.append(new_account)
    save_accounts(accounts)
    print("Аккаунт успешно создан.")

def save_accounts(accounts):
    with open("accounts.json", "w") as file:
        json.dump(accounts, file)

def login(username, password):
    if not file_exists("accounts.json"):
        print("Ошибка 2: Аккаунт не существует.")
        return False

    with open("accounts.json", "r") as file:
        accounts = json.load(file)

    for account in accounts:
        if account["username"] == username and account["password"] == password:
            print("Вход выполнен.")
            return True

    print("Ошибка 3: Неправильное имя пользователя или пароль.")
    return False

def main():
    if not file_exists("accounts.json"):
        accounts = []
    else:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)

    if login(username, password):
        lines = "Это круто!", "Попробуй снова - не сдавайся!", username + ", ЭТО ТЫ?!", username + ":~$ sudo python3 SpectraOS.py", "(Не)Интересные новости: " + username + " вошёл в систему!", "ААААААААААААААААААА"
        random_line = random.choice(lines)
        print("Проверка зависимостей...")
        os.system('pip install fs')
        os.system('pip install wget')
        print("Загрузка...")
        w(3)
        import fs
        import fs.copy
        import wget
        mem_fs = fs.open_fs('mem://')
        mem_fs.makedirs('root')
        mem_fs.makedirs('root/home')
        mem_fs.makedirs('root/home/user')
        mem_fs.makedirs('root/home/user/downloads')
        mem_fs.makedirs('root/home/user/documents')
        mem_fs.makedirs('root/home/user/videos')
        mem_fs.makedirs('root/home/user/pictures')
        mem_fs.makedirs('root/home/user/AppDatas')
        mem_fs.makedirs('root/home/user/AppDatas/Local')
        mem_fs.makedirs('root/home/user/AppDatas/Global')
        with mem_fs.open('root/home/magic.txt', 'w') as magicdoc:
            magicdoc.write(random_line)
        with fs.open_fs(".") as os_fs:
            fs.copy.copy_fs(mem_fs, os_fs)
        os.system('cls||clear')
        print("SpectraOS 1.1")
        print(random_line)
        while True:
             com = input('/root/home/user/>')
             if com == "changelog":
                 print("1. Исправлен баг с echo")
                 print("2. Добавил обновление по воздуху")
                 print("3. Блокнот теперь не wii, а wiim")
                 print("4. Переписал текст при загрузке")
                 print("5. Больше текстов после входа (наверное)")
                 #проблема. добавлю потом
                 #print("6. Добавил Gemini (ЭЭЭЭЭкспириментально)")
                 print("6. Пофиксил команду changelog")
                 w(3)
                 print("В С Ё !")
             if com == "update":
                import requests
                import hashlib

                def download_file(url, filename):
                    response = requests.get(url)
                    with open(filename, 'wb') as file:
                        file.write(response.content)

                def calculate_hash(filename):
                    with open(filename, 'rb') as file:
                    	content = file.read()
                    	return hashlib.sha256(content).hexdigest()
                    
                url = 'https://raw.githubusercontent.com/BlankHtmlPage/SpectraOS/main/spectraosupdated.py'
                filename = 'spectraosupdated.py'
                print("Проверка наличий обновлений...")
                download_file(url, filename)
                existing_hash = calculate_hash("SpectraOS.py")
                new_hash = calculate_hash('spectraosupdated.py')
                if existing_hash != new_hash:
                    print("Обновление найдено! Обновляемся...")
                    os.system('python updater.py')
                    exit(15)
                else:
                    print('У Вас установлена последняя версия (1.1)')
             if com == "deleteyourself":
                 os.system('del SpectraOS.py||rm SpectraOS.py')
             if com == "restart":
                 os.system('py SpectraOS.py')
                 os.exit(666)
             if com == "bear":
                 print("Пасхалка!")
             if com == "echo":
                 text = input("Введите текст для отображения: >")
                 print(text)
             if com == "wiim":
                 filenam = input('Введите название файла чтобы создать/редактировать: >')
                 with open('root/home/user/documents/' + filenam + ".txt", "w") as note:
                     wiitw = input('Введите то что надо вписать: >')
                     note.write(wiitw)
             if com == "wget":
                 url = input('Введите ссылку до файла: >')
                 file = wget.download(url, out='root/home/user/downloads')
                 print(file)
             if com == "exit":
                 print("Сохраняем ваши настройки...")
                 w(3)
                 print("Записываем несохраненные данные на диск...")
                 w(3)
                 print("SpectraOS выключается...")
                 w(2)
                 exit(666)
             if com == "help":
                 print("Команды: changelog, help, about, deleteaccount, dir, wget, wiim, info, echo, restart, exit")
             if com == "about":
                  print("SpectraOS 1.1")
                  print(random_line)
                  print("Сборка от 24.08.2024")
             if com == "deleteaccount":
                  utd = input('Введите имя пользователя, которого необходимо удалить: >')
                  delete_account(utd)
             if com == "dir":
                 mem_fs.tree()

if __name__ == '__main__':
    tl = input('(в)ход или (р)егистрация?: (р=регистрация, в=вход. Только маленькие буквы!) ')
    if tl == "в":
        username = input('Введите имя пользователя: >')
        password = input('Введите пароль: >')
        main()
    if tl == "р":
        username = input('Придумайте имя аккаунта: >')
        password = input('Придумайте пароль: >')
        if username and password == "":
            print("Ошибка -1: Вы должны ввести имя аккаунта и пароль")
            exit(666)
        create_account(username, password)
        main()

