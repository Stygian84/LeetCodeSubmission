class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split()
        ls2=[]
        for item in ls:
            ls2.append(item[::-1])
        return " ".join(ls2)