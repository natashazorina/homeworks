import re
f = open("text_first_task.txt", "r")
data = f.read()
data1 = (list(filter(None, re.split('\W', data))))
print(data1)
d = 1
f = open('text.txt', 'w')
for index in data1:
    if d%20 == 0:
       f.write(index + '\n')
       d += 1
    else:
        f.write(index + " ")
        d += 1 
f.close()
