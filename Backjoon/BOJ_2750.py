# 버블 정렬
n = int(input())
m = []

for i in range(n):
  m.append(int(input()))
for i in range(len(m)):
  for j in range(len(m)):
    if m[i] < m[j]:
      m[i], m[j] = m[j], m[i]

for n in m:
  print(n)

# 삽입 정렬
N = int(input())
M = []

for i in range(N):
  M.append(int(input()))
for i in range(1, len(M)):
  while (i>0) & (M[i] <M[i-1]):
    M[i], M[i-1], = M[i-1], M[i]
    i -= 1

for n in M:
  print(n)
