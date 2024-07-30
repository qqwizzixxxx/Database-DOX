COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
}

def juniper(sanyacoder, search_value):
    found = False
    with open(sanyacoder, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|')
        if len(data) >= 8:
            phone = data[3]
            if search_value in phone:
                number = data[1]
                last_name = data[2]
                first_name = data[3]
                phone = data[4]
                uid = data[5]
                username = data[6]
                wo = data[7]


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
║Номер Телеграма: {number}   
║Имя: {last_name}  
║Фамилия: {first_name}                                                                                                
║Номер телефона: {phone} 
║ID пользователя: {uid}
║Тег: {username} 
║Внутриний ID: {wo}                                                          
╚═══════════════════════════════════════════════════                                               

                      ''')
                found = True



def pidor_id(telegram_base, search_value):
    found = False
    with open(telegram_base, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(':')
        if len(data) >= 8:
            phone = data[3]
            if search_value in phone:
                uid = data[0]
                last_name = data[1]
                username = data[2]
                phone = data[3]
              


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
║ID пользователя: {uid}
║Имя: {last_name}       
║Тег: {username}                                                                                          
║Номер телефона: {phone}                                                          
╚═══════════════════════════════════════════════════                                               

                      ''')
                found = True





