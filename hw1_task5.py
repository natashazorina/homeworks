import re
f = open("passwords.txt", "r")
data = f.read()
word_list = data.split()
d = 0
a = 0
for word in word_list:
    def validate():
        while True:
            if len(word) < 6:
                break
            elif re.search('[0-9]',word) is None:
                break
            elif re.search('[a-z]',word) is None: 
                break
            elif re.search('[A-Z]',word) is None: 
                break
            elif re.search('[$,/?|\.^&*#@!]',word) is None: 
                break
            else:
                print(word)
                break
 
    validate()
