n, k = map(int, input().split())
a_list = list(map(int, input().split()))

print(sorted(a_list)[k-1])