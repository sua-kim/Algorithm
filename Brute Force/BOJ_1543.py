'''
document = input()
word = input()
document = document.replace(word, '*')
cnt = 0
for i in document:
    if i == '*':
        cnt += 1
print(cnt)
'''

document = input()
word = input()
index = 0
cnt = 0
while index + len(word) < len(document) - 1:
    if document[index:index+len(word)] == word:
        index += len(word)
        cnt += 1
    else:
        index += 1
print(cnt)