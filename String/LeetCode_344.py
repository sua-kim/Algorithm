'''
LeetCode_344 - 문자열 뒤집기
'''

# 1차로 내가 푼 코드 -> Wrong Answer
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s = s[::-1]
        return s

# 2차로 내가 푼 코드
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            char = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = char
        return s

# 해결방법1: 공간복잡도가 O(1)이라는 제약으로 인해 발생한 문제
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        return s

# 해결방법2
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        return s