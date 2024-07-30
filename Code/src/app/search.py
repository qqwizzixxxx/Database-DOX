COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
}

def stalin(file, search_value):
    found = False
    with open(file, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            phone = data[7]
            if search_value in phone:
                ID = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                thrid_name = data[4]
                date_bithday = data[5]
                Sex = data[6]
                email = data[8]
                rol0 = data[9]
                rol = data[10]
                rol1 = data[11]
                clas = data[12]
                class_letter = data[13]
                kyrc = data[14]
                Country = data[15]
                School_County = data[16]
                Region = data[17]
                School_Name = data[18]
                Adress = data[19]
                Work = data[20]
                School_Type = data[21]
                Organization = data[22]
                Kod = data[23]
                Vector = data[24]
                Vizov = data[25]
                


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
║ Телефон: {phone}                                                            
║ Роль в конкурсе: {rol}                                                      
║ ID: {ID}                                                                    
║ Роль в событии: {rol1}                                                      
║ Дата Регистрации: {registration_date}                                       
║ Класс: {clas}                                                               
║ Имя: {first_name}                                                           
║ Буква {class_letter}                                                        
║ Фамилия: {last_name}                                                        
║ Курс: {kyrc}                                                                
║ Отчество: {thrid_name}                                                      
║ Гражданство: {Country}                                                      
║ Дата Рождения: {date_bithday}                                               
║ Страна обучения: {School_County}                                            
║ Пол: {Sex}                                                                                                                              
║ Регион: {Region}                                                             
║ Почта: {email}                                                              
║ Муниципальное образование: {School_Name}                                   
║ Роль: {rol0}                                                                
║ Адрес: {Adress}                                                             
║ Должность: {Work}                                                           
║ Тип: {School_Type}                                                          
║ Организация: {Organization}                                                 
║ Код: {Kod}                                                                                                                             
║ Вектор: {Vector}                                                            
║ Вызов: {Vizov}                                                              
╚═════════════════════════════════════════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')

def phone1(file3, search_value):
    found = False
    with open(file3, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            phone = data[7]
            if search_value in phone:
                ID = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                thrid_name = data[4]
                date_bithday = data[5]
                Sex = data[6]
                email = data[8]
                rol0 = data[9]
                rol = data[10]
                rol1 = data[11]
                clas = data[12]
                class_letter = data[13]
                kyrc = data[14]
                Country = data[15]
                School_County = data[16]
                Region = data[17]
                School_Name = data[18]
                Adress = data[19]
                Work = data[20]
                School_Type = data[21]
                Organization = data[22]
                Kod = data[23]
                Vector = data[24]
                Vizov = data[25]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═════════════════════════════════════════════════════════════════════════════
║ Телефон: {phone}                                                            
║ Роль в конкурсе: {rol}                                                      
║ ID: {ID}                                                                    
║ Роль в событии: {rol1}                                                      
║ Дата Регистрации: {registration_date}                                       
║ Класс: {clas}                                                               
║ Имя: {first_name}                                                           
║ Буква {class_letter}                                                        
║ Фамилия: {last_name}                                                        
║ Курс: {kyrc}                                                                
║ Отчество: {thrid_name}                                                      
║ Гражданство: {Country}                                                      
║ Дата Рождения: {date_bithday}                                               
║ Страна обучения: {School_County}                                            
║ Пол: {Sex}                                                                                                                              
║ Регион: {Region}                                                             
║ Почта: {email}                                                              
║ Муниципальное образование: {School_Name}                                   
║ Роль: {rol0}                                                                
║ Адрес: {Adress}                                                             
║ Должность: {Work}                                                           
║ Тип: {School_Type}                                                          
║ Организация: {Organization}                                                 
║ Код: {Kod}                                                                                                                             
║ Вектор: {Vector}                                                            
║ Вызов: {Vizov}                                                              
╚═════════════════════════════════════════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')
        
def alfa_bank(alfa, search_value):
    found = False
    with open(alfa, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 4:
            phone = data[4]
            if search_value in phone:
                ID = data[0]
                FIO = data[1]
                Bithday = data[2]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═══════════════════════════════════════════════════════════════════════
║ Телефон: {phone}                                                                                                  
║ ID: {ID}                                                              
║ Фио: {FIO}                                                            
║ Дата Рождения: {Bithday}                                              
╚═══════════════════════════════════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')
        
def good_eye(good, search_value):
    found = False
    with open(good, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 3:
            phone = data[1]
            if search_value in phone:
                ID = data[0]
                FIO = data[3]
                Bithday = data[4]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═════════════════════════════════════════════════════════════════════
║ Телефон: {phone}                                                     
║ ID: {ID}                                                             
║ Имя: {FIO}                                                           
║ Фамилия: {Bithday}                                                   
╚══════════════════════════════════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')
        
        
def peremena(file1, search_value):
    found = False
    with open(file1, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            phone = data[7]
            if search_value in phone:
                ID = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                thrid_name = data[4]
                date_bithday = data[5]
                Sex = data[6]
                email = data[8]
                rol0 = data[9]
                rol = data[10]
                rol1 = data[11]
                clas = data[12]
                class_letter = data[13]
                kyrc = data[14]
                Country = data[15]
                School_County = data[16]
                Region = data[17]
                School_Name = data[18]
                Adress = data[19]
                Work = data[20]
                School_Type = data[21]
                Organization = data[22]
                Kod = data[23]
                Vector = data[24]
                Vizov = data[25]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═════════════════════════════════════════════════════════════════════════════
║ Телефон: {phone}                                                            
║ Роль в конкурсе: {rol}                                                      
║ ID: {ID}                                                                    
║ Роль в событии: {rol1}                                                      
║ Дата Регистрации: {registration_date}                                       
║ Класс: {clas}                                                               
║ Имя: {first_name}                                                           
║ Буква {class_letter}                                                        
║ Фамилия: {last_name}                                                        
║ Курс: {kyrc}                                                                
║ Отчество: {thrid_name}                                                      
║ Гражданство: {Country}                                                      
║ Дата Рождения: {date_bithday}                                               
║ Страна обучения: {School_County}                                            
║ Пол: {Sex}                                                                                                                              
║ Регион: {Region}                                                             
║ Почта: {email}                                                              
║ Муниципальное образование: {School_Name}                                   
║ Роль: {rol0}                                                                
║ Адрес: {Adress}                                                             
║ Должность: {Work}                                                           
║ Тип: {School_Type}                                                          
║ Организация: {Organization}                                                 
║ Код: {Kod}                                                                                                                             
║ Вектор: {Vector}                                                            
║ Вызов: {Vizov}                                                              
╚═════════════════════════════════════════════════════════════════════════════
                ''')
                found = True
                

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')
        
def phone0(file2, search_value):
    found = False
    with open(file2, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            phone = data[7]
            if search_value in phone:
                ID = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                thrid_name = data[4]
                date_bithday = data[5]
                Sex = data[6]
                email = data[8]
                rol0 = data[9]
                rol = data[10]
                rol1 = data[11]
                clas = data[12]
                class_letter = data[13]
                kyrc = data[14]
                Country = data[15]
                School_County = data[16]
                Region = data[17]
                School_Name = data[18]
                Adress = data[19]
                Work = data[20]
                School_Type = data[21]
                Organization = data[22]
                Kod = data[23]
                Vector = data[24]
                Vizov = data[25]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═════════════════════════════════════════════════════════════════════════════
║ Телефон: {phone}                                                            
║ Роль в конкурсе: {rol}                                                      
║ ID: {ID}                                                                    
║ Роль в событии: {rol1}                                                      
║ Дата Регистрации: {registration_date}                                       
║ Класс: {clas}                                                               
║ Имя: {first_name}                                                           
║ Буква {class_letter}                                                        
║ Фамилия: {last_name}                                                        
║ Курс: {kyrc}                                                                
║ Отчество: {thrid_name}                                                      
║ Гражданство: {Country}                                                      
║ Дата Рождения: {date_bithday}                                               
║ Страна обучения: {School_County}                                            
║ Пол: {Sex}                                                                                                                              
║ Регион: {Region}                                                             
║ Почта: {email}                                                              
║ Муниципальное образование: {School_Name}                                   
║ Роль: {rol0}                                                                
║ Адрес: {Adress}                                                             
║ Должность: {Work}                                                           
║ Тип: {School_Type}                                                          
║ Организация: {Organization}                                                 
║ Код: {Kod}                                                                                                                             
║ Вектор: {Vector}                                                            
║ Вызов: {Vizov}                                                              
╚═════════════════════════════════════════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')
  
def p2hone1(file4, search_value):
    found = False
    with open(file4, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            phone = data[7]
            if search_value in phone:
                ID = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                thrid_name = data[4]
                date_bithday = data[5]
                Sex = data[6]
                email = data[8]
                rol0 = data[9]
                rol = data[10]
                rol1 = data[11]
                clas = data[12]
                class_letter = data[13]
                kyrc = data[14]
                Country = data[15]
                School_County = data[16]
                Region = data[17]
                School_Name = data[18]
                Adress = data[19]
                Work = data[21]
                School_Type = data[21]
                Organization = data[22]
                Kod = data[23]
                Vector = data[24]
                Vizov = data[25]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔════════════════════════════════════════════════════════════════════════════
║ Телефон: {phone}                                                            
║ Роль в конкурсе: {rol}                                                      
║ ID: {ID}                                                                    
║ Роль в событии: {rol1}                                                      
║ Дата Регистрации: {registration_date}                                       
║ Класс: {clas}                                                               
║ Имя: {first_name}                                                           
║ Буква {class_letter}                                                        
║ Фамилия: {last_name}                                                        
║ Курс: {kyrc}                                                                
║ Отчество: {thrid_name}                                                      
║ Гражданство: {Country}                                                      
║ Дата Рождения: {date_bithday}                                               
║ Страна обучения: {School_County}                                            
║ Пол: {Sex}                                                                                                                              
║ Регион: {Region}                                                             
║ Почта: {email}                                                              
║ Муниципальное образование: {School_Name}                                   
║ Роль: {rol0}                                                                
║ Адрес: {Adress}                                                             
║ Должность: {Work}                                                           
║ Тип: {School_Type}                                                          
║ Организация: {Organization}                                                 
║ Код: {Kod}                                                                                                                             
║ Вектор: {Vector}                                                            
║ Вызов: {Vizov}                                                              
╚═════════════════════════════════════════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')

def wb(fl, search_value):
    found = False
    with open(fl, 'r') as file:
        lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            phone = data[3]
            if search_value in phone:
                kod = data[0]
                Full_name = data[1]
                Komment = data[2]
                phone1 = data[4]
                work_phone = data[5]
                email_adress = data[6]
                adress = data[7]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═══════════════════════════════════════════
║ Телефон: {phone}                          
║ Код: {kod}                                
║ ФИО: {Full_name}                          
║ Имя: {Komment}                            
║ Телефон 2: {phone1}                       
║ Рабочий телефон: {work_phone}             
║ Почта: {email_adress}                      
║ Адресс: {adress}                          
╚═══════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')
        
def yandex(file5, search_value):
    found = False
    with open(file5, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 5:
            phone = data[0]
            if search_value in phone:
                first_name = data[1]
                full_name = data[2]
                email = data[3]
                address_info = data[4].split(',')

                address_city = address_info[0]
                address_street = address_info[1]
                address_house = address_info[2]
                address_entrance = address_info[3]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
                
╔═══════════════════════════════════════════                                       		
║ Телефон: {phone}
║ Имя: {first_name}
║ Полное имя: {full_name}
║ Электронная почта: {email}
║ Город: {address_city}
║ Улица: {address_street}
║ Дом: {address_house}
║ Подъезд: {address_entrance}                                                        
╚═══════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')

def data(floup, search_value):
    found = False
    with open(floup, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
            phone = data[7]
            if search_value in phone:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                email = data[8]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]  
                municipal_education = data[18]  
                institution_name = data[21]  
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═══════════════════════════════════════════                                                                
║ ID пользователя: {data[0]}
║ Дата регистрации: {data[1]}
║ Фамилия: {data[2]}
║ Имя: {data[3]}
║ Отчество: {data[4]}
║ Дата рождения: {data[5]}
║ Пол: {data[6]}
║ Телефон: {data[7]}
║ Почта: {data[8]}
║ Роль: {data[9]}
║ Класс: {data[13]}
║ Адрес: {data[19]}
║ Страна: {data[16]}
║ Гражданство: {data[15]}
║ Регион: {data[17]}
║ Муниципальное образование: {data[18]}
║ Наименование учреждения: {data[20]}                                                           
╚═══════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')
        
def negr(number4, search_value):
    found = False
    with open(number4, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 8:
            phone = data[6]
            if search_value in phone:
                first_name = data[0]
                middle_name = data[1]
                last_name = data[2]
                birthday = data[3]
                gender = data[4]
                email = data[5]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═══════════════════════════════════════════ 
║ Имя: {data[0]}                                                             
║ Отчество: {data[1]}
║ Фамилия: {data[2]}
║ Дата рождения: {data[3]}
║ Пол: {data[4]}
║ Почта: {data[5]}
║ Телефон: {data[6]}                                                                
╚═══════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')
        
def celevay(file7, search_value):
    found = False
    with open(file7, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 6:
            phone = data[5]
            if search_value in phone:
                email = data[0]
                email = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═══════════════════════════════════════════ 
║ Почта: {data[0]}                                                             
║ Почта: {data[1]}
║ Фамилия: {data[2]}
║ Имя: {data[3]}
║ Отчество: {data[4]}
║ Телефон: {data[5]}                                                               
╚═══════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')
        

def alfa_qwe(arram, search_value):
    found = False
    with open(arram, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 5:
            phone = data[4]
            if search_value in phone:
                full_name = data[0]
                citizenship = data[1]
                birthday = data[5]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═══════════════════════════════════════════ 
║ ФИО: {data[0]}                                                             
║ Гражданство: {data[1]}
║ Дата рождения: {data[5]}
║ Телефон: {data[6]}                                                          
╚═══════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')


def ior(asd, search_value):
    found = False
    with open(asd, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 5:
            phone = data[2]
            if search_value in phone:
                birthday = data[0]
                full_name = data[1]
                address = data[3]
                


                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═══════════════════════════════════════════ 
║ Дата рождения: {data[0]}
║ ФИО: {data[1]}                                                             
║ Телефон: {data[2]}
║ Адрес: {data[3]}                                                     
╚═══════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')
        
def nekr(pauset, search_value):
    found = False
    with open(pauset, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 5:
            phone = data[4]
            if search_value in phone:
                last_name = data[0]
                first_name = data[1]
                middle_name = data[2]
                email = data[3]
                birthday = data[5]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═══════════════════════════════════════════ 
║ Фамилия: {data[0]}
║ Имя: {data[1]}                                                        
║ Отчество: {data[2]}
║ Почта: {data[3]}     
║ Телефон: {data[4]}      
║ Дата рождения: {data[5]}                                         
╚═══════════════════════════════════════════
                ''')
                found = True


    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')
                    
def helix_number(helix_db, search_value):
    found = False
    with open(helix_db, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(",")
        if len(data) >= 5:
            phone = data[6]
            if search_value in phone:
                surname = data[0]
                name = data[1]
                otch = data[2]
                birdh_day = data[3]
                male = data[4]
                email = data[5]
                

                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                                          
╔═══════════════════════════════════════════════════════════════                                                                            
║ Телефон: {phone}
║ Фамилия: {surname}
║ Имя: {name}
║ Отчество: {otch}
║ Дата рождения: {birdh_day}
║ Пол: {male}
║ Эл. Почта: {email}         
╚═══════════════════════════════════════════════════════════════
                ''')
                found = True

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')
                            

def klsaas(satoshibd, search_value):
    found = False

    with open(satoshibd, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',') 
        if len(data) >= 5:
            email = data[0]
            Fname = data[1]
            lname = data[2]
            phone = data[3]
            instagram = data[4]

            if search_value in phone:
                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                       
╔═════════════════════════════════════════════════════════════════ 
║ Почта: {email}
║ Имя: {Fname}
║ Фамилия: {lname}
║ Телефон: {phone}
║ Инстаграм: {instagram}                                                      
╚═════════════════════════════════════════════════════════════════                                              
                 
                  ''')

                found = True

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')   


def helper(satoshimatra, search_value):
    found = False

    with open(satoshimatra, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',') 
        if len(data) >= 5:
            region = data[0]
            phone= data[1]
            adress = data[2]
            section = data[3]
            podm = data[4]

            if search_value in phone:
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
║ Регион: {region}
║ Телефон: {phone}
║ Адресс: {adress}
║ Категория: {section}
║ Товары: {podm}                                                     
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')

def msiafter(getandnumb, search_value):
    found = False

    with open(getandnumb, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 3:
            phone = data[0]
            name = data[1]
            hzto = data[2]

            if search_value in phone:
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
║ Телефон: {phone}
║ Имя в Базе 1: {name}
║ Имя в Базе 2: {hzto}                                                     
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                         

def kletka(para, search_value):
    found = False

    with open(para, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 2:
            phone = data[0]
            fio = data[1]

            if search_value in phone:
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
║ Телефон: {phone}
║ ФИО: {fio}                                                   
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')       

def gena(para2, search_value):
    found = False

    with open(para2, 'r', encoding='windows-1251') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 3:
            phone = data[0]
            fio = data[1]
            address = data[2]

            if search_value in phone:
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
║ Телефон: {phone}
║ ФИО: {fio}
║ Адрес: {address}                                                     
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                

def roda(para3, search_value):
    found = False

    with open(para3, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 2:
            phone = data[0]
            tags = data[1]
           

            if search_value in phone:
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
║ Телефон: {phone}
║ Тег: {tags}                                                  
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                


def litra(para4, search_value):
    found = False

    with open(para4, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 2:
            phone = data[0]
            tags = data[1]

            if search_value in phone:
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
║ Телефон: {phone}
║ Тег: {tags}                                                    
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                

def tarakan(para5, search_value):
    found = False

    with open(para5, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 2:
            phone = data[0]
            tags = data[1]

            if search_value in phone:
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
║ Телефон: {phone}
║ Тег: {tags}                                                   
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                

def neznau(para9, search_value):
    found = False

    with open(para9, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 3:
            fio = data[0]
            dateofbirth = data[1]
            passport = data[2] 
            address = data[3] 
            phone = data[4]

            if search_value in phone:
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
║ ФИО: {fio}
║ Дата рождения: {dateofbirth}
║ Пасспорт: {passport}   
║ Адрес: {address}   
║ Телефон: {phone}                                                           
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                

def vedro(para7, search_value):
    found = False

    with open(para7, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|') 
        if len(data) >= 5:
            fio = data[0]
            dateofbirth = data[1]
            passport = data[2] 
            address = data[3] 
            phone = data[4]

            if search_value in phone:
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
║ ФИО: {fio}
║ Дата рождения: {dateofbirth}
║ Пасспорт: {passport}   
║ Адрес: {address}   
║ Телефон: {phone}                                               
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                

def brat(para8, search_value):
    found = False

    with open(para8, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 5:
            fio = data[0]
            dateofbirth = data[1]
            passport = data[2] 
            address = data[3] 
            phone = data[4]

            if search_value in phone:
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
║ ФИО: {fio}
║ Дата рождения: {dateofbirth}
║ Пасспорт: {passport}   
║ Адрес: {address}   
║ Телефон: {phone}                                               
╚═══════════════════════════════════════════════════════════════════                                  
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                

def mnelen(para10, search_value):
    found = False

    with open(para10, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 5:
            fio = data[0]
            dateofbirth = data[1]
            passport = data[2] 
            address = data[3] 
            phone = data[4]

            if search_value in phone:
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
║ ФИО: {fio}
║ Дата рождения: {dateofbirth}
║ Пасспорт: {passport}   
║ Адрес: {address}   
║ Телефон: {phone}                                                      
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                

def univer(para11, search_value):
    found = False

    with open(para11, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 7:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            dbirthdate = data[5]
            cmainphonenum = data[6]

            if search_value in cmainphonenum:
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
║ ID: {icusid}    
║ ФИО: {ccusfullname}  
║ ИНН: {ccusinn}  
║ Страна: {ccitizenship} 
║ Пол: {cgender}     
║ Дата рождения: {dbirthdate} 
║ Телефон: {cmainphonenum}                                   
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')       

def mucl1(file9, search_value):
    found = False

    with open(file9, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(' ') 
        if len(data) >= 4:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 

            if search_value in ccitizenship:
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
║ Фамилия: {ccusinn}  
║ Номер телефона: {ccitizenship}                                   
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')  

def mucl2(file10, search_value):
    found = False

    with open(file10, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|') 
        if len(data) >= 7:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            dbirthdate = data[5]
            cmainphonenum = data[6]

            if search_value in dbirthdate:
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
║ ФИО: {icusid}    
║ Дата рождения: {ccusfullname}  
║ Адрес: {ccusinn}  
║ Паспорт: {ccitizenship} 
║ Кем выдан: {cgender}     
║ Номер телефона: {dbirthdate} 
║ Почта: {cmainphonenum}                                   
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')  

def mucl3(file11, search_value):
    found = False

    with open(file11, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',') 
        if len(data) >= 6:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            dbirthdate = data[5]

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
║ Номер телефона: {icusid}    
║ ФИО: {ccusfullname}  
║ Город: {ccusinn}  
║ Улица: {ccitizenship} 
║ Номер дома: {cgender}     
║ Тариф: {dbirthdate}                                   
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                                   

def mucl4(file12, search_value):
    found = False

    with open(file12, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',') 
        if len(data) >= 5:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 

            if search_value in cgender:
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

        

def mucl5(file13, search_value):
    found = False

    with open(file13, 'r', encoding='windows-1251') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|') 
        if len(data) >= 13:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            dbirthdate = data[5]
            cmainphonenum = data[6]
            big = data[7]
            big1 = data[8]
            big2 = data[9]
            big3 = data[10]
            big4 = data[11]
            big5 = data[12]


            if search_value in big4:
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
║ Город: {icusid}    
║ Район: {ccusfullname}  
║ Улица: {ccusinn}  
║ Дом: {ccitizenship} 
║ Строение: {cgender}     
║ Кол-во подьездов: {dbirthdate} 
║ Кол-во этажей: {cmainphonenum}  
║ Кол-во квартир: {big}     
║ Номер квартиры: {big1} 
║ Номер комнаты: {big2}
║ ФИО: {big3}     
║ Номер телефона: {big4} 
║ Тех.информация: {big5}                                 
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')  

def mucl7(file14, search_value):
    found = False

    with open(file14, 'r', encoding='utf-8') as file:
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

            if search_value in dbirthdate:
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
         
def mucl6(file8, search_value):
    found = False

    with open(file8, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(' ') 
        if len(data) >= 6:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            dbirthdate = data[5]

            if search_value in cgender:
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
║ Место: {icusid}    
║ ФИО: {ccusfullname}  
║ Город: {ccusinn}  
║ Почта: {ccitizenship} 
║ Номер телефона: {cgender}     
║ Должность: {dbirthdate}                                    
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                                   


def sbc(notsbj, search_value):
    found = False

    with open(notsbj, 'r', encoding='windows-1251') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 5:
            icusid = data[0]
            number = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4]

            if search_value in number:
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
║ ID: {icusid}    
║ Номер (Без +7): {number}  
║ ФИО: {ccusinn}  
║ Адрес: {ccitizenship} 
║ Паспортные данные: {cgender}                                      
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')      

def gaz(file15, search_value):
    found = False

    with open(file15, 'r', encoding='utf-8') as file:
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

            if search_value in cgender:
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
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}') 

def dns(file16, search_value):
    found = False

    with open(file16, 'r', encoding='utf-8') as file:
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
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')    

def spasibo2(file18, search_value):
    found = False

    with open(file18, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|') 
        if len(data) >= 3:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 

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
║ Номер телефона: {icusid}    
║ Дата рождения: {ccusfullname}  
║ Почта: {ccusinn}                    
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}') 

def spasibo(file17, search_value):
    found = False

    with open(file17, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|') 
        if len(data) >= 3:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 

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
║ Номер телефона: {icusid}    
║ Дата рождения: {ccusfullname}                     
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                                        


def zatr(file19, search_value):
    found = False

    with open(file19, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|') 
        if len(data) >= 4:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 

            if search_value in ccitizenship:
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
║ Имя: {icusid}    
║ Фамилия: {ccusfullname}  
║ Почта: {ccusinn}  
║ Номер телефона: {ccitizenship}                 
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}') 

def pidr(file20, search_value):
    found = False

    with open(file20, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(' ') 
        if len(data) >= 4:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 

            if search_value in ccitizenship:
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
║ Имя: {icusid}    
║ Фамилия: {ccusfullname}  
║ Почта: {ccusinn}  
║ Номер телефона: {ccitizenship}                 
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')         

def love(file21, search_value):
    found = False

    with open(file21, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(' ') 
        if len(data) >= 6:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            dataros = data[4]
            gorod = data[5]

            if search_value in ccitizenship:
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
║ Почта: {ccusfullname}  
║ ФИО: {ccusinn}  
║ Номер телефона: {ccitizenship}   
║ Дата рождения: {dataros} 
║ Город: {gorod}             
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                 

def ebat(file22, search_value):
    found = False

    with open(file22, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(' ') 
        if len(data) >= 5:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            dataros = data[4]


            if search_value in ccitizenship:
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
║ ФИО Отправителя: {icusid}    
║ Город Получения: {ccusfullname}  
║ ФИО Получятеля: {ccusinn}  
║ Номер телефона получателя: {ccitizenship}   
║ Город отправки: {dataros}             
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')           

def ebat1(file23, search_value):
    found = False

    with open(file23, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',') 
        if len(data) >= 10:
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

            if search_value in ccitizenship:
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
║ Имя: {icusid}    
║ Фамилия: {ccusfullname}  
║ Почта: {ccusinn}  
║ Номер телефона: {ccitizenship} 
║ Дата рождения: {cgender}     
║ Часовой пояс: {dbirthdate}   
║ Адрес: {login} 
║ Страна: {snus}  
║ Skype: {skype}
║ Логин: {skype2}                  
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')         

def ebat2(file24, search_value):
    found = False

    with open(file24, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(' ') 
        if len(data) >= 5:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 

            if search_value in cgender:
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
║ Фамилия: {icusid}    
║ Имя: {ccusfullname}  
║ Отчество: {ccusinn}  
║ Город: {ccitizenship} 
║ Номер телефона: {cgender}                      
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')     

def ebat3(file25, search_value):
    found = False

    with open(file25, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 7:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            happy = data[5]
            reg = data[6]

            if search_value in cgender:
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
║ Фамилия: {ccusinn}  
║ Отчество: {ccitizenship} 
║ Номер телефона: {cgender}  
║ Дата рождения: {happy}
║ Регион: {reg}                   
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                         

def ebat4(file26, search_value):
    found = False

    with open(file26, 'r', encoding='windows-1251') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|') 
        if len(data) >= 4:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 

            if search_value in ccusinn:
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
║ ФИО: {icusid}    
║ Дата рождения: {ccusfullname}  
║ Номер телефона: {ccusinn}  
║ Почта: {ccitizenship}                 
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')    

def ebat5(file27, search_value):
    found = False

    with open(file27, 'r', encoding='windows-1251') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(':') 
        if len(data) >= 8:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            happy = data[5]
            reg = data[6]
            mail = data[7]

            if search_value in ccitizenship:
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
║ Системный Номер: {icusid}    
║ 2 Системный номер: {ccusfullname}  
║ ФИО: {ccusinn}  
║ Номер телефона: {ccitizenship} 
║ Полный адрес: {cgender}  
║ Стационарный телефон: {happy}
║ Населённый пункт: {reg}    
║ Почта: {mail}               
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')    

def ebat6(file28, search_value):
    found = False

    with open(file28, 'r', encoding='windows-1251') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',') 
        if len(data) >= 37:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            happy = data[5]
            reg = data[6]
            io = data[7]
            io1 = data[8]
            io2 = data[9]
            io3 = data[10]
            io4 = data[11]
            io5 = data[12]
            io6 = data[13]
            io7 = data[14]
            hz = data[15]
            hz1 = data[16]
            hz2 = data[17]
            hz3 = data[18]
            hz4 = data[19]
            hz5 = data[20]
            hz6 = data[21]
            hz7 = data[22]
            hz8 = data[23]
            hz9 = data[24]
            hz10 = data[25]
            hz11 = data[27]
            hz12 = data[28]
            hz13 = data[29]
            hz14 = data[30]
            hz15 = data[31]
            hz16 = data[32]
            hz17 = data[33]
            hz18 = data[34]
            hz19 = data[35]
            hz20 = data[36]




            if search_value in hz3:
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
║ Партнёр ID: {icusid}    
║ Код: {ccusfullname}  
║ Номер партнёра: {ccusinn}  
║ Код категории: {ccitizenship} 
║ Код группы: {cgender}  
║ Имя группы: {happy}
║ Фамилия: {reg}
║ Имя: {io}
║ Отчество: {io1}
║ Дата рождение: {io2}                 
║ Пол: {io3}
║ Флагоперация: {io3}
║ Дата операции: {io4}
║ Возвраст: {io5}
║ ХЗ Что : {io6}
║ Тоже хз: {io7}
║ база хуйня: {hz}
║ докс: {hz1}
║ ФИО: {hz2}
║ Номер телефона: {hz3}
║ ID Страны: {hz4}
║ Регион: {hz5}
║ Город: {hz6}
║ ХЗ: {hz7}
║ Улица: {hz8}
║ Номер дома: {hz9}
║ Строительство: {hz10}
║ Номер комнаты: {hz11}
║ Валидный Номер: {hz12}
║ СМС: {hz13}
║ 2 СМС: {hz14}
║ Почта: {hz15}
║ Название коммуникации: {hz16}
║ Номер паспорта: {hz17}
║ Тип паспорта: {hz18}
║ Кем выдан: {hz19}
║ Дата выдачи: {hz20}
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')    

def ebat7(file29, search_value):
    found = False

    with open(file29, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',') 
        if len(data) >= 7:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            happy = data[5]
            reg = data[6]

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
║ ФИО: {icusid}    
║ Номер телефона: {ccusfullname}  
║ Страна: {ccusinn}  
║ Город: {ccitizenship} 
║ Банк: {cgender}  
║ Баланс: {happy}
║ Перевод: {reg}                   
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')    

def ebat8(file30, search_value):
    found = False

    with open(file30, 'r', encoding='windows-1251') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|') 
        if len(data) >= 7:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            happy = data[5]
            reg = data[6]

            if search_value in cgender:
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
║ Системный номер: {icusid}    
║ Номер телефона: {ccusfullname}  
║ Абонент: {ccusinn}  
║ Улица: {ccitizenship} 
║ Дом: {cgender}  
║ Квартира: {happy}
║ Дата: {reg}                   
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Продолжаю поиск.{COLOR_CODE["RESET"]}')                                            

def ebat9(file31, search_value):
    found = False

    with open(file31, 'r', encoding='windows-1251') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|') 
        if len(data) >= 8:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 
            happy = data[5]
            reg = data[6]
            mail = data[7]

            if search_value in cgender:
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
║ Фамилия: {icusid}    
║ Имя: {ccusfullname}  
║ Отчество: {ccusinn}  
║ Дата рождения: {ccitizenship} 
║ Номер телефона: {cgender}  
║ СНИЛС: {happy}
║ ИНН: {reg}
║ Почта: {mail}                   
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

    if not found:
        print(f'{COLOR_CODE["BLUE"]}Ошибка. В базе данных нету данного номера телефона. Поиск завершён.{COLOR_CODE["RESET"]}')         