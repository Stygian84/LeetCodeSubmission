class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(x):
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
        s=set()

        for num in nums:
            s.add(num)
            s.add(reverse(num))
        return len(s)