'''
알파윷 A
- 10번의 결과를 4명에게 분배하는 모든 경우의 수를 구하고 K번째 수열 출력
'''

K = int(input())
result = [0] * 10
count = 0

def recursion(index, K):
    global count
    if index >= 10:
        count += 1
        if count == K:
            print(' '.join(map(str, result)))
            exit(0)
        return
    for i in range(1, 5):
        result[index] = i
        recursion(index+1, K)
        result[index] = 0

recursion(0, K)