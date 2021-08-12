'''
LeetCode_125 - 유효한 팰린드롬
'''

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