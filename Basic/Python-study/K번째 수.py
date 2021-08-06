T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    number_list = list(map(int, input().split()))
    number_list = number_list[s-1:e]
    number_list.sort()
    print("#%d %d" % (i+1, number_list[k-1]))

