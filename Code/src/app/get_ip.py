import socket
import requests
import os 

COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
}

def get_ip():
        os.system("cls")
        print(f'''{COLOR_CODE["BLUE"]}
                                                                                 
                                                                                 
                                                                                     
                                                                                     
▓█████▄  ▄▄▄     ▄▄▄█████▓ ▄▄▄       ▄▄▄▄    ▄▄▄        ██████ ▓█████ 
▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒████▄    ▓█████▄ ▒████▄    ▒██    ▒ ▓█   ▀ 
░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄  ▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ▒███   
░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░█▀  ░██▄▄▄▄██   ▒   ██▒▒▓█  ▄ 
░▒████▓  ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒░▒████▒
 ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒░ ░
 ░ ▒  ▒   ▒   ▒▒ ░   ░      ▒   ▒▒ ░▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░ ░ ░  ░
 ░ ░  ░   ░   ▒    ░        ░   ▒    ░    ░   ░   ▒   ░  ░  ░     ░   
   ░          ░  ░              ░  ░ ░            ░  ░      ░     ░  ░
 ░                                        ░                           
                                                                                                                                                                                            
''')                
        ip = input(f'{COLOR_CODE["BLUE"]}[@] Введите айпи: ')

try:
        ip = socket.gethostbyname(ip) # type: ignore
        
        infoList1 = requests.get(f"http://ipwho.is/{ip}")
        infoList = infoList1.json()
        
        if infoList.get("success"):
            print(f'''{COLOR_CODE["BLUE"]}
 ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███     
███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄ 
███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██ 
███    ███   ███        ███▌ ███   ███     ███   ▀ 
███    ███ ▀███████████ ███▌ ███   ███     ███     
███    ███          ███ ███  ███   ███     ███     
███    ███    ▄█    ███ ███  ███   ███     ███     
 ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀   
                                                    
╔═══════════════════════════════════════════════════   
║Айпи адресс:   {infoList["ip"]}
║Успех:         {infoList["success"]}
║Тип:           {infoList["type"]}
║Континент:     {infoList["continent"]}
║Страна:        {infoList["country"]}
║Регион:        {infoList["region"]}
║Город:         {infoList["city"]}
║Почтовый код:  {infoList["postal"]}
║Столица:       {infoList["capital"]}
╚═══════════════════════════════════════════════════                     
''')
        else:
            print(f'''{COLOR_CODE["BLUE"]}
 ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███     
███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄ 
███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██ 
███    ███   ███        ███▌ ███   ███     ███   ▀ 
███    ███ ▀███████████ ███▌ ███   ███     ███     
███    ███          ███ ███  ███   ███     ███     
███    ███    ▄█    ███ ███  ███   ███     ███     
 ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀   
                                                    
╔═══════════════════════════════════════════════════ 
║IP:           {infoList["ip"]}
║Success:      {infoList["success"]}
║Message:      {infoList["message"]}
╚═══════════════════════════════════════════════════ 
''')
except Exception as e:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. Не удалось определить IP: {e}')
