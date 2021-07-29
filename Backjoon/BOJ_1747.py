N = int(input())
if(N==1):
    print(2)
else:
    while True:
        flag=1
        if(str(N)==str(N)[::-1]):
            for i in range(2,int(N**0.5)+1):
                if N%i == 0:
                    flag=0
                    break
            if flag:
                print(N)
                break
        N+=1
