# MyProfile app



def check_digital(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def word_year(age):
    if 11 <= age % 100 <= 19:
        years = 'лет'
    elif age % 10 == 1:
        years = 'год'
    elif 2 <= age % 10 <= 4:
        years = 'года'
    else:
        years = 'лет'
    return years


def only_digit(stroke):
    number = ''
    for simbol in stroke:
        if simbol == '0' or ('1' <= simbol <= '9'):
            number += simbol
    return number


def personal_information():
    print(f'Имя:             {name}\n'
          f'Возраст:         {age} {word_year(age)}\n'
          f'Телефон:         +{only_digit(phone_number)}\n'
          f'E-mail:          {email}\n'
          f'Почтовый индекс: {only_digit(post_index)}\n'
          f'Почтовый адрес   {post_mail}\n'
          '\nДополнительная информация:\n',
            information)


SEPARATOR = '------------------------------------------'

# User profile.  
name = ''
age = 0
phone_number = ''
email = ''
post_index = ''
post_mail = ''
information = ''

# Information bizness.  
ogrnip = ''
inn = ''
checking_account = ''
name_bank = ''
bic = ''
correspondent_account = ''

print('Приложение MyProfile\n'
      'Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # Main menu.  
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ\n'
          '1 - Ввести или обновить информацию\n'
          '2 - Вывести информацию\n'
          '0 - Завершить работу')

    main_menu = int(input('Введите номер пункта меню: '))
    
    if main_menu == 0:
        break
    elif main_menu == 1:
        #submenu: edit info.
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ\n'
                  '1 - Личная информация\n'
                  '2 - Информация о предпринимателе\n'
                  '0 - Назад')

            submenu = int(input('Введите номер пункта меню: '))
            
            if submenu == 0:
                break
            elif submenu == 1:
                # Input personal info.  
                name = input('Введите имя: ')
                
                while 1:
                    # Validate user age.  
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                phone_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                email = input('Введите адрес электронной почты: ')
                post_index = input('Введите почтовый индекс: ')
                post_mail = input('Введите почтовый адрес: ')
                information = input('Введите дополнительную информацию:\n')
            elif submenu == 2:
                # Input informations of bizness.  
                while True:
                    ogrnip = int(input('Введите ОГРНИП: '))
                    if check_digital(ogrnip) == 15:
                        break
                    else:
                        print('ОГРНИП должен содержать 15 цифр')
                        
                inn = input('Введите ИНН: ')
                 
                while True:
                    checking_account = int(input('Введите расчётный счёт: '))
                    if check_digital(checking_account) == 20:
                        break
                    else:
                        print('Расчётный счёт должен быть 20 цифр')
                 
                name_bank = input('Введите название Банка: ')
                bic = input('Введите БИК: ')
                correspondent_account = input('Введите корреспондентский счёт: ')
            else: print('Введите корректный пункт меню')
    elif main_menu == 2:
        # submenu: print information.  
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ\n'
                  '1 - Личная информация\n'
                  '2 - Вся информация\n'
                  '0 - Назад')

            submenu = int(input('Введите номер пункта меню: '))
            
            if submenu == 0:
                break
            elif submenu == 1:
                # Print personal information.  
                print(SEPARATOR)
                personal_information()
            elif submenu == 2:
                # Print full information.  
                print(SEPARATOR)
                personal_information()
                # Print information of bizness.  
                print(f'\nИнформация о предпренимателе\n'
                      f'ОГРНИП:         {ogrnip}\n'
                      f'ИНН:            {inn}\n'
                      f'Название банка: {name_bank}\n'
                      f'БИК банка       {bic}\n'
                      f'Р/с             {checking_account}\n'
                      f'К/с             {correspondent_account}\n')
            else:   
                print('Введите корректный пункт меню')
    else:       
        print('Введите корректный пункт меню')
