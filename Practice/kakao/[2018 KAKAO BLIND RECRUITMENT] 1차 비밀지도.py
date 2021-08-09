def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        row = ""
        num = arr1[i]|arr2[i]
        for j in range(n):
            if num % 2 == 0:
                square = ' '
            else:
                square = '#'
            row = square + row
            num //= 2
        answer.append(row)
    return answer
