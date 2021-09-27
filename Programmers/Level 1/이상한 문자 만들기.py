def solution(s):
    s_list = list(s.split(' '))
    answer = []
    for str in s_list:
        word = ''
        for i in range(len(str)):
            word += (str[i].upper() if i%2==0 else str[i].lower())
        answer.append(word)
    answer = ' '.join(answer)
    return answer