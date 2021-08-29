import time

num_list = [int(input()) for _ in range(9)]

start = time.time()

max_num = max(num_list)
print(max_num)
print(num_list.index(max_num)+1)

end = time.time()
print(f'소요시간: {end-start}')