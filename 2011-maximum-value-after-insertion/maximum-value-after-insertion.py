class Solution:
    def maxValue(self, n: str, x: int) -> str:
        sign = 1
        if n[0]=="-":
            sign = -1
        
        str_x = str(x)
        for i in range(len(n)):
            digit = n[i]
            if digit == "-":
                continue
            if sign == -1:
                if digit>str_x:
                    return n[:i] + str_x + n[i:]
            else:
                if digit<str_x:
                    return n[:i] + str_x + n[i:]

        return n + str_x
