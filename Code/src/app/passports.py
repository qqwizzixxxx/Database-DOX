import os
import random

COLOR_CODE = {
        "BLUE": "\033[34m",
        "RESET": "\033[0m",
    }
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
print("[$] Сколько пасспортов сгенерировать? Максимум - 1000:")
try:
            count = int(input())
            if count > 1000:
                print("Ошибка: Вы ввели число больше 1000.")
            else:
                with open("Базы\data43", "r", encoding="utf-8") as file:
                    lines = file.readlines()

                generated_lines = [random.choice(lines) for _ in range(count)]
                print("Сгенерировано:")
                for line in generated_lines:
                    print(line, end="")
except ValueError:
     print("Ошибка: Введено некорректное число.")
     input("Нажмите Enter, чтобы продолжить...") 
