import os
import random

COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
}


download_folder = os.path.expanduser("~/Downloads/Databsekey")

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

for i in range(1):
    random_number = random.randint(10**15, 10**16 - 1)  
    filename = os.path.join(download_folder, f"mullvadkey.txt")
    
    with open(filename, 'w') as file:
        file.write(str(random_number))
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
                                                                                                                            
                                                                                                         
       ╔═════════════════════════════════════════╗  ╔═════════════════════════════════════════╗
       ║     Статус Валидности: Не определён     ║  ║ Ключ сохранён в вашей папке: "Загрузки" ║
       ╚═════════════════════════════════════════╝  ╚═════════════════════════════════════════╝
              
                                ''')          

        
 


