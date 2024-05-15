class Solution:
    def countAsterisks(self, s: str) -> int:
        ls=s.split("|")
        result=0
        for idx in range(len(ls)):
            if idx%2==0:
                result+=ls[idx].count("*")
        return result
        