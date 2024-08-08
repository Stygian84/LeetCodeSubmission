class Solution:
    def maxValue(self, n: str, x: int) -> str:
        sign = 1
        if n[0]=="-":
            sign = -1
        
        for i in range(len(n)):
            digit = n[i]
            if digit == "-":
                continue
            if sign == -1:
                if digit>str(x):
                    return n[:i] + str(x) + n[i:]
            else:
                if digit<str(x):
                    return n[:i] + str(x) + n[i:]

        return n + str(x)
