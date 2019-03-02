import re
 
def validate():
    while True:
        password = input("Введите пароль: ")
        if len(password) < 6:
            print("Ваш пароль должен быть минимум 6 симболов")
        elif re.search('[0-9]',password) is None:
            print("Ваш пароль должен содержать цифры")
        elif re.search('[a-z]',password) is None: 
            print("Ваш пароль должен содержать буквы")
        elif re.search('[A-Z]',password) is None: 
            print("Ваш пароль должен содержать заглавные буквы")
        elif re.search('[$#@,*.\|/&!^?]',password) is None: 
            print("Ваш пароль должен символы пунктуации")
        else:
            print("Хороший пароль!")
            break
 
validate()
