a = int(input())
b = list(map(int, list(input())))
three = a*b[2]
four = a*b[1]
five = a*b[0]
six = three + 10*four + 100*five
print(three)
print(four)
print(five)
print(six)