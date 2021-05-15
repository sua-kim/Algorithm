def solution(array, commands):
    answer = []
    for set in commands:
        i = set[0]
        j = set[1]
        k = set[2]
        answer.append(sorted(array[i-1:j])[k-1])

    return answer

if __name__ == "__main__":
    #solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))