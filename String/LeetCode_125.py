'''
LeetCode_125 - 유효한 팰린드롬
'''

# 나의 풀이

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_list = []

        for character in s.lower():
            if character in 'abcdefghijklmnopqrstuvwxyz0123456789':
                string_list.append(character)
        if string_list == string_list[-1::-1]:
            return True
        else:
            return False


# 풀이 1: 리스트로 변환
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in str:
            if char.isalnum():
                strs.append(char.lower())
        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

# 풀이 2: 데크 자료형을 이용한 최적화 (10장 이후 시도)

# 풀이 3: 슬라이싱 사용
import re
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
