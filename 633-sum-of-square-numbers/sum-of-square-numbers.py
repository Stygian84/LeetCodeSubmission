class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(c**0.5)
        while a<=b:
            total=a**2+b**2
            if total==c:
                return True
            elif total<c:
                a+=1
            else:
                b-=1
        return False