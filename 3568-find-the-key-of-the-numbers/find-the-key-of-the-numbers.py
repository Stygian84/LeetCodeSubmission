class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        
        res = []

        num1 = str(num1).zfill(4)
        num2 = str(num2).zfill(4)
        num3 = str(num3).zfill(4)

        i = 0
        while i < 4:
            res.append(min(num1[i],num2[i],num3[i]))
            i+=1

        return int("".join(res))