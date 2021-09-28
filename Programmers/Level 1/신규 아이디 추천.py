def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    str = 'abcdefghijklmnopqrstuvwxyz-_.0123456789'
    new_id = [char for char in new_id if char in str]
    # 3단계
    cnt = 0
    answer = []
    for i in range(len(new_id)):
        if new_id[i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt >= 2:
            continue
        answer.append(new_id[i])
    # 4단계
    if answer[0] == '.':
        del answer[0]
    if len(answer)!=0 and answer[-1] == '.':
        del answer[-1]
    # 5단계
    if not answer:
        answer.append('a')
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        del answer[-1]
    # 7단계
    if len(answer) <= 2:
        final = answer[-1]
        while len(answer) < 3:
            answer.append(final)
    answer = ''.join(answer)
    return answer