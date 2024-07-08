class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ls1 = sorted(s1)
        ls2 = sorted(s2)

        increasing=True
        decreasing=True
        for a,b in zip(ls1,ls2):
            if ord(a)>ord(b):
                decreasing=False
            elif ord(a)<ord(b):
                increasing=False
            if not increasing and not decreasing:
                return False
        return increasing or decreasing