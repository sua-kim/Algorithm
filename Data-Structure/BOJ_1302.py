N = int(input())
book_dict = dict()

for _ in range(N):
    book = input()
    if book not in book_dict:
        book_dict[book] = 1
    else:
        book_dict[book] += 1

target = max(book_dict.values())
result = []

for book, number in book_dict.items():
    if number == target:
        result.append(book)

print(sorted(result)[0])