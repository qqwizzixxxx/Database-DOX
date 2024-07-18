COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
}
def pizda(lgin, search_value):
    found = False

    with open(lgin, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',') 
        if len(data) >= 5:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 

            if search_value in icusid:
                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═══════════════════════════════════════════════════════════════════             
║ Логин: {icusid}    
║ Город: {ccusfullname}  
║ ФИО: {ccusinn}  
║ Почта: {ccitizenship} 
║ Номер телефона: {cgender}                                        
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')  


def cep(log, search_value):
    found = False

    with open(log, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',') 
        if len(data) >= 8:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            dbirthdate = data[5]
            login = data[6]
            snus = data[7]

            if search_value in login:
                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═══════════════════════════════════════════════════════════════════             
║ Почта: {icusid}    
║ Имя: {ccusfullname}  
║ Очество: {ccusinn}  
║ Фамилия: {ccitizenship} 
║ Дата рождения: {cgender}     
║ Номер телефона: {dbirthdate}   
║ Логин: {login} 
║ СНИЛС: {snus}                                
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')
                
                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')  

def cuka(mot, search_value):
    found = False

    with open(mot, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|') 
        if len(data) >= 3:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 

            if search_value in ccusfullname:
                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═══════════════════════════════════════════════════════════════════             
║ Логин: {icusid}    
║ Номер телефона: {ccusfullname}  
║ Почта: {ccusinn}                    
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Поиск завершён.{COLOR_CODE["RESET"]}')         