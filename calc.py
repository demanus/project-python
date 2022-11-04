# post_index_input = input('Введите почтовый индекс: ')
# post_index = ''
# for simbol in post_index_input:
#     if simbol == '0' or ('1' <= simbol <= '9'):
#         post_index += simbol
# print(post_index)

def only_digit(stroke):
    phone_number = ''
    for simbol in stroke:    
        if simbol == '0' or ('1' <= simbol <= '9'):
            phone_number += simbol
    return phone_number
    


# phone_input = input('Введите номер телефона (+7ХХХХХХХХХХ): ')

# print('+' + only_digit(phone_input))


# print('Имя:             ', 'name')               
# print('Возраст:         ', 'age, word_year(age)')                                
# print('Телефон:         ', ' + only_digit(phone_number)')                
# print('E-mail:          ', 'email')                
# print('Почтовый индекс: ', 'only_digit(post_index)')                
# print('Почтовый адрес   ', 'post_mail')

print(f'Имя:             {1} name\n'
      f'Возраст:         {1} age, word_year(age)\n'
      f'Телефон:         {1} + only_digit(phone_number)\n')
