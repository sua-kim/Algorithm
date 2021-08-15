'''
LeetCode_819 - 가장 흔한 단어
'''

# 처음 제출한 코드
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        edit_paragraph = re.sub(r'[^a-zA-Z0-9 ]', ' ', paragraph.lower())

        max = 0
        common_words = ''

        for str in list(edit_paragraph.split()):
            if str in banned:
                continue
            if max < list(edit_paragraph.split()).count(str):
                max = edit_paragraph.count(str)
                common_words = str

        return common_words