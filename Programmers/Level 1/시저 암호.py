def solution(s, n):
    answer = ''
    s = list(s)
    for string in s:
        index = ord(string)
        if index == 32:
            answer += string
            continue
        if index >= 97:
            answer += chr(index + n if index + n - 96 <= 26 else index + n - 26)
            continue
        answer += chr(index + n if index + n - 64 <= 26 else index + n - 26)

    return answer