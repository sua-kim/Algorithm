'''
BOJ_2609 - 최대공약수와 최소공배수
'''

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a, b = map(int, input().split())
g = gcd(a, b)
print(g)
print(a*b//g)