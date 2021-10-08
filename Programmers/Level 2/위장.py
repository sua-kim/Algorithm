def solution(clothes):
    answer = 1
    cloth_dict = {}
    for cloth in clothes:
        if cloth[1] in cloth_dict.keys():
            cloth_dict[cloth[1]] += 1
        else:
            cloth_dict[cloth[1]] = 1
    for key in list(cloth_dict):
        answer *= (cloth_dict[key]+1)
    return answer - 1