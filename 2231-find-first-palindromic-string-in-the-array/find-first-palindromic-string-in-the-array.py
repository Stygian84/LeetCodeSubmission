class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for item in words:
            if item==item[::-1]:
                return item
        return ""