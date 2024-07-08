class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ls1 = sorted(list(s1))
        ls2 = sorted(list(s2))

        increasing=True
        decreasing=True
        for a,b in zip(ls1,ls2):
            if ord(a)>ord(b):
                decreasing=False
            elif ord(a)<ord(b):
                increasing=False
        return increasing or decreasing