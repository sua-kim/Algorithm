T = int(input())
case_list = [input() for _ in range(T)]

for i in range(T):
    year = case_list[i][0:4]
    month = case_list[i][4:6]
    day = case_list[i][6:8]
    if int(month) in [1, 3, 5, 7, 8, 10, 12] and 1 <= int(day) <= 31:
        print(f'#{i+1} {year}/{month}/{day}')
    elif int(month) == 2 and 1 <= int(day) <= 28:
        print(f'#{i+1} {year}/{month}/{day}')
    elif int(month) in [4, 6, 9, 11] and 1 <= int(day) <= 30:
        print(f'#{i+1} {year}/{month}/{day}')
    else:
        print(f'#{i+1} -1')
