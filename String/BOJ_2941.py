a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()
for i in a:
    alpha = alpha.replace(i, 'a')
print(len(alpha))