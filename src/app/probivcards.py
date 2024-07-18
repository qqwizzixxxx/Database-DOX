

COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
}

def kotily(son, search_value):
    found = False
    with open(son, 'r', encoding='windows-1251') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 9:
            cards = data[3]
            if search_value in cards:
                fio = data[0]
                birthday = data[1]
                passports = data[2]
                cards = data[3]
                srok = data[4]
                sykablyad = data[5]
                limit = data[6]
                phone = data[7]
                dates = data[8]


                print(f'''{COLOR_CODE["BLUE"]}
 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═══════════════════════════════════════════════════   
║ФИО: {fio}   
║Дата рождения: {birthday}  
║Пасспорт: {passports}                                                                                                
║Номер карты: {cards} 
║Срок действ. карты: {srok}
║Номер счета карты: {sykablyad} 
║Лимт: {limit}      
║Номер телефона: {phone}
║Дата оформления: {dates}                                                   
╚═══════════════════════════════════════════════════                                               

                      ''')
                found = True
