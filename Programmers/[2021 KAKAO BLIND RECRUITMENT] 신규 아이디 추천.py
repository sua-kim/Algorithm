import re

def solution(new_id):
    new_id = new_id.lower()
    characters = "abcdefghijklmnopqrstuvwxyz-_.1234567890"
    new_id = ''.join(x for x in new_id if x in characters)
    new_id = re.sub('\.{2,}', '.', new_id)
    new_id = re.sub('^.', '', new_id)
    new_id = new_id.replace('{.}$', '')

    if new_id == '':
        new_id += 'a'
    if len(new_id) >= 15:
        new_id = new_id[:15]
        new_id = new_id.replace(r'.$', '')
    answer = new_id
    if len(new_id) <= 2:
        while(len(new_id)==3):
            answer = new_id
            answer += new_id[len(new_id)-1]
    return answer
