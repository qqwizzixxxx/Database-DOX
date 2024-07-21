COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
}


def vkbd(vkdad, search_value):
    found = False
    with open(vkdad, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 21:
            uid = data[0]
            if search_value in uid:
                uid = data[0]
                last_name = data[2]
                pol = data[3]
                country = data[4]
                city = data[5]
                let = data[6]
                roshdenie = data[7]
                rodcity = data[8]
                namevk = data[9]
                poloshenie = data[10]
                namepart = data[11]
                lastpart = data[12]
                twitter = data[13]
                ebatwitter = data[14]
                syktwitter = data[15]
                liver = data[16]
                koliver = data[17]
                skype = data[18]
                mobphone = data[19]
                domphone = data[20]

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
║ID аккаунта: {uid}  
║Имя: {last_name}  
║Пол: {pol}                                                                                                
║Страна: {country} 
║Город: {city}
║Возвраст: {let} 
║Дата рождения: {roshdenie} 
║Родной город: {rodcity}
║Короткая ссылка: {namevk}
║Семейное положение: {poloshenie}
║Имя партнёра:{namepart}
║Фамилия партнёра: {lastpart}
║Твитер: {twitter}
║Короткая ссылка Твитера: {ebatwitter}
║Ссылка на твитер: {syktwitter}
║Livejournal: {liver}                                                        
║ссылка на Livejournal: {koliver}
║Skype: {skype}
║Моб.Телефон: {mobphone}
║Дом.телефон {domphone}
╚═══════════════════════════════════════════════════                                               

                      ''')
                found = True

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                 

def vksuk(vknorm, search_value):
    found = False

    with open(vknorm, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',') 
        if len(data) >= 12:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            dbirthdate = data[5]
            login = data[6]
            snus = data[7]
            skype = data[8]
            skype2 = data[9]
            skype3 = data[10]
            skype4 = data[11]

            if search_value in skype4:
                print(f'''{COLOR_CODE["BLUE"]}

 ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███     
███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄ 
███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██ 
███    ███   ███        ███▌ ███   ███     ███   ▀ 
███    ███ ▀███████████ ███▌ ███   ███     ███     
███    ███          ███ ███  ███   ███     ███     
███    ███    ▄█    ███ ███  ███   ███     ███     
 ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀                                    
╔═══════════════════════════════════════════════════════════════════             
║ Почта: {icusid}    
║ Дата рождения: {ccusfullname}  
║ Имя: {ccusinn}  
║ Фамилия: {ccitizenship} 
║ Номер телефона: {cgender}     
║ Отчество: {dbirthdate}   
║ Класс: {login} 
║ Школа: {snus}  
║ Skype: {skype}
║ Номер региона: {skype2}
║ Роль: {skype3}        
║ ВК: {skype4}                    
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Поиск завершён.{COLOR_CODE["RESET"]}')                 