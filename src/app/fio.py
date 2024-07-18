COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
}

def fiobd(fiobad, search_value):
    found = False
    with open(fiobad, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 5:
            fiofull = data[2]
            if search_value in fiofull:
                number = data[0]
                email = data[1]
                fiofull = data[2]
                dolsh = data[3]
                phone = data[4]
                


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
║Номер пользователя: {number}
║Почта: {email}                                                     
║ФИО: {fiofull}                                                      
║Должность: {dolsh} 
║Телефон: {phone}                                                     
╚═════════════════════════════════════════════════════════════════════════════
                ''')
                found = True
