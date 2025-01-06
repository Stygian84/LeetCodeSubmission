class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for letter in s:
            if letter.isalpha():
                res.append(letter.lower())
            elif letter.isdigit():
                res.append(letter)
        
        return res==res[::-1]