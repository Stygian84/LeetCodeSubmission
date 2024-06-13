class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res=""
        while a!=b and a>0 and b>0:
            if a>b:
                res+='aa'
                a-=2
                res+='b'
                b-=1
            elif a<b:
                res+='bb'
                b-=2
                res+='a'
                a-=1
            else:
                break

        while a==b and a>0:
            res+='a'
            res+='b'
            a-=1
            b-=1
        return res+'a'*a+'b'*b