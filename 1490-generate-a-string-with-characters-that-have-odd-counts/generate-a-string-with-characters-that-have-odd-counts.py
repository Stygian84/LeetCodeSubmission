class Solution:
    def generateTheString(self, n: int) -> str:
        if n==1:
            return "a"
        if n%2==0:
            result="a"*(n-1)+"b"
        else:
            result="a"*(n-2)+"b"+"c"
        return result
        