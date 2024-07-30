

COLOR_CODE = {
    "BLUE": "\033[34m",    
    "RESET": "\033[0m",
}

def piska(file5, search_value):
    found = False

    with open(file5, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')  
        if len(data) >= 21:  
            email = data[8]
            if search_value in email:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                phone = data[7]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]  
                municipal_education = data[18]  
                institution_name = data[20]  
                
                print(f'''{COLOR_CODE["BLUE"]}

 ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███  ███▀▀▀██▄   ███    ███ ███    ███ 
███▌ ███   ███   ███    █▀  ███    ███ 
███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███  ███   ███   ███        ███    ███ 
███  ███   ███   ███        ███    ███ 
█▀    ▀█   █▀    ███         ▀██████▀  
                                               
╔══════════════════════════════════════════════════════════════════════════                                                                                                                
║ID пользователя: {data[0]}
║Дата регистрации: {data[1]}
║Фамилия: {data[2]}
║Имя: {data[3]}
║Отчество: {data[4]}
║Дата рождения: {data[5]}
║Пол: {data[6]}
║Телефон: {data[7]}
║Почта: {data[8]}
║Роль: {data[9]}
║Класс: {data[13]}
║Адрес: {data[19]}
║Страна: {data[16]}
║Гражданство: {data[15]}
║Регион: {data[17]}
║Муниципальное образование: {data[18]}
║Наименование учреждения: {data[20]}                                                  
╚═══════════════════════════════════════════════════════════════════════════                                                   
                     
                      ''')
                found = True

    
 

def xyina(file, search):
    found = False
    with open(file, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            mail = data[8]
            if search in mail:
                ID = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                thrid_name = data[4]
                date_bithday = data[5]
                Sex = data[6]
                mail = data[8]
                phone = data[7]
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
                                       
╔═════════════════════════════════════════════════════════════════════════════════
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
║ Почта: {mail}                                                              
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

 

def xyeta(file1, search):
    found = False
    with open(file1, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            mail = data[8]
            if search in mail:
                ID = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                thrid_name = data[4]
                date_bithday = data[5]
                Sex = data[6]
                mail = data[8]
                phone = data[7]
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
║ Почта: {mail}                                                              
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
                        

def blyad(file2, search):
    found = False
    with open(file2, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            mail = data[8]
            if search in mail:
                ID = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                thrid_name = data[4]
                date_bithday = data[5]
                Sex = data[6]
                mail = data[8]
                phone = data[7]
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
║ Почта: {mail}                                                              
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

            
def syka(file3, search):
    found = False
    with open(file3, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            mail = data[8]
            if search in mail:
                ID = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                thrid_name = data[4]
                date_bithday = data[5]
                Sex = data[6]
                mail = data[8]
                phone = data[7]
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
║ Почта: {mail}                                                              
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

                       

def nevoryicode(file4, search):
    found = False
    with open(file4, 'r', encoding='utf-8') as file:
       lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 7:
            mail = data[8]
            if search in mail:
                ID = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                thrid_name = data[4]
                date_bithday = data[5]
                Sex = data[6]
                mail = data[8]
                phone = data[7]
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
║ Почта: {mail}                                                              
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

def jopa(fileblyad, search_value):
    found = False

    with open(fileblyad, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';') 
        if len(data) >= 5:
            icusid = data[0]
            ccusfullname = data[1] 
            ccusinn = data[2] 
            ccitizenship = data[3] 
            cgender = data[4] 

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
║ Город: {ccusfullname}  
║ ФИО: {ccusinn}  
║ Почта: {ccitizenship} 
║ Номер телефона: {cgender}                                        
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 

def iiiop(filesuka, search_value):
    found = False

    with open(filesuka, 'r', encoding='utf-8') as file:
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
║ Место: {icusid}    
║ ФИО: {ccusfullname}  
║ Город: {ccusinn}  
║ Почта: {ccitizenship} 
║ Номер телефона: {cgender}     
║ Должность: {dbirthdate}                                    
╚═══════════════════════════════════════════════════════════════════                            
                 
                  ''')

                found = True 
                