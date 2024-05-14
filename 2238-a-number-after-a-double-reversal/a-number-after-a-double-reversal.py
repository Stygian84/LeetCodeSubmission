class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num*1==0:
            return True
        s=str(num)
        print(s)
        if s[-1]=="0" or s[0]=="0":
            return False
        return True