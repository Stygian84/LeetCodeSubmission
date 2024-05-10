class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def atoi(s):
            rtr=0
            for c in s:
                rtr=rtr*10 + ord(c) - ord('0')

            return rtr
        return str(atoi(num1)*atoi(num2))