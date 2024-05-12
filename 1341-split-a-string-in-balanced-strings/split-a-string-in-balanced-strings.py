class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        R=0
        L=0
        for item in s:
            if item =="R":
                R+=1
            else:
                L+=1
            if R==L:
                R=0
                L=0
                count+=1
        return count

        