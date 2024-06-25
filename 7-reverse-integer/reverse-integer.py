class Solution:
    def reverse(self, x: int) -> int:
        min_value=-2**31
        max_value=2**31-1

        sign=1
        if x<0:
            sign=-1
        
        x=abs(x)

        res=0
        while x != 0:
            digit = x % 10
            x //= 10

            if res > (max_value - digit) // 10:
                return 0

            res = res * 10 + digit

        return sign * res
        '''
        res=int(str(x)[::-1]) * sign

        if res<min_value or res>max_value:
            return 0
        return res'''