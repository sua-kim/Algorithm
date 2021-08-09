'''
BOJ_2309 - 일곱 난쟁이
'''

# 처음 제출 코드
from itertools import combinations

def find_real(nine_list):
    seven_dwarf = list(combinations(nine_list, 7))
    for i in seven_dwarf:
        if sum(i) == 100:
            return list(i)
            
nine_dwarf = []
for i in range(9):
    nine_dwarf.append(int(input()))
    
real_dwarf = sorted(find_real(nine_dwarf))

for n in real_dwarf:
    print(n)

# pythonic 코드 수정
from itertools import combinations
nine_dwarf=[int(input()) for i in range(9)]
seven_dwarf = list(combinations(nine_dwarf,7))
for i in seven_dwarf:
    if sum(i)==100:
        print(*sorted(i),sep='\n')
        break
