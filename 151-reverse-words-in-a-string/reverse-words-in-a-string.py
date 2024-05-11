class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s.reverse()
        result=" ".join(s)
        return result