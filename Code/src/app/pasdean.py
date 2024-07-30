COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
} 
def internet(pas, search_value):
    found = False

    with open(pas, 'r', encoding='windows-1251') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|') 
        if len(data) >= 3:
            icusid = data[0]
            ccusfullname = data[1] 

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
║ Номер телефона: {icusid}    
║ Пароль: {ccusfullname}                                    
╚═══════════════════════════════════════════════════════════════════ 
  ''')

                found = True 