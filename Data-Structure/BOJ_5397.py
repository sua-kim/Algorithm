test_case = int(input())

for _ in range(test_case):
    keyboard_input = list(input())
    password = list()
    remain = list()

    for key in keyboard_input:
        if key == '<':
            if password:
                remain.append(password.pop())
        elif key == '>':
            if remain:
                password.append(remain.pop())
        elif key == '-':
            if password:
                password.pop()
        else:
            password.append(key)
    remain.reverse()
    password += remain
    print(''.join(password))