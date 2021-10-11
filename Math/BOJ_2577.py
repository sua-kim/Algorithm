a = int(input())
b = int(input())
c = int(input())
n_list = list(map(int, list(str(a*b*c))))
result = [0] * 10
for n in n_list:
    result[n] += 1
for i in range(10):
    print(result[i])