print("введите interest: ")
a = input()
a = float(a)
a = a * 0.4
print("введите talent: ")
b = input()
b = float(b)
b = b * 0.2
print("введите diligence: ")
c = input()
c = float(c)
c = c * 0.4 + b + a
if c < 10:
    print("студент не справился")
else:
    print("cтудент справился")
