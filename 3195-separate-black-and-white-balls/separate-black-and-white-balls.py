class Solution:
    def minimumSteps(self, s: str) -> int:

        n = len(s)
        count = 0
        zero = 0
        for i in range(n-1,-1,-1):
            if s[i]=="1":
                count+=zero
            else:
                zero+=1

        return count