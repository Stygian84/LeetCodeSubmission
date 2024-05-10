class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.find(needle)
        except:
            return -1