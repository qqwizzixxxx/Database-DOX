COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
}

def interbb(facebb, search_value):
    found = False
    with open(facebb, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 8:
            fbid = data[0]
            if search_value in fbid:
                fbid = data[0]
                phone = data[1]
                profid = data[2]
                pddr = data[3]
                roddom = data[4]
                country = data[5]
                work = data[6]
                valid = data[7]
                
                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔══════════════════════════════════════════════════════════════════════════════
║ ID пользователя: {fbid}                                                            
║ Телефон: {phone}                                                      
║ ID профиля: {profid}                                                                    
║ Имя Фамилия: {pddr}                                                      
║ Город: {roddom}                                       
║ Страна: {country}                                                               
║ Работа: {work}                                                           
║ Валидность: {valid}                                                                                                                      
╚═════════════════════════════════════════════════════════════════════════════
                ''')
                found = True