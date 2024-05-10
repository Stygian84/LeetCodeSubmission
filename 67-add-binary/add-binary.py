class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        b=b[::-1]
        a=a[::-1]
        result=""
        one=0
        two=0
        for i in range(len(a)):
            one+=2**i*int(a[i])
        for i in range(len(b)):
            two+=2**i*int(b[i])
        print(a,b)
        result=bin(one+two)[2:]
        return result
        