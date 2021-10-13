n = int(input())
book_list = {}
result = []
for _ in range(n):
    book = input()
    if book not in book_list:
        book_list[book] = 0
    book_list[book] += 1
target = max(book_list.values())
for key in list(book_list):
    if book_list[key] == target:
        result.append(key)
print(sorted(result)[0])