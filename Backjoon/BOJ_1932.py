n = int(input())
result = []

side=2 
for i in range(n):
    result.append(list(map(int,input().split())))
for i in range(1,n): 
    for j in range(side):
        if j==0: 
            result[i][j] +=result[i-1][j]
        elif i==j:
            result[i][j] +=result[i-1][j-1]
        else:
            result[i][j] +=max(result[i-1][j],result[i-1][j-1])
    side+=1 
print(max(result[n-1]))
