document = list(input())
word = list(input())

document_status = [True] * len(document)
word_length = len(word)
count = 0

for i in range(len(document)-word_length+1):
    if document_status[i] and document[i:i+word_length]==word:
        for j in range(i,i+word_length):
            document_status[j] = False
        count += 1

print(count)