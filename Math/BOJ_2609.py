'''
BOJ_2609 - 최대공약수와 최소공배수
'''

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

a, b = map(int, input().split())
g = gcd(a, b)
print(g)
print(a*b//g)