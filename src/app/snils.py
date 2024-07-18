COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
}

def jokeybd(zxcbad, search_value):
    found = False
    with open(zxcbad, 'r', encoding='windows-1251') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split('|')
        if len(data) >= 9:
            snils = data[7]
            if search_value in snils:
                name = data[1]
                last = data[2]
                fist = data[3]
                burthday = data[4]
                sex = data[5]
                passport = data[6]
                snils = data[7]
                dokument = data[8]
                address = data[9]
                

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
║ Фамилия: {name} 
║ Имя: {last}
║ Отчество: {fist}                                                       
║ Дата рождения: {burthday}                                                      
║ Пол: {sex}                                                                                                                         
║ СНИЛС: {address}  
║ Документ: {snils}                                     
║ Адрес:  {passport}   
║ Код точки проживания: {dokument}                                                                                                 
╚═════════════════════════════════════════════════════════════════════════════
                ''')
                found = True
