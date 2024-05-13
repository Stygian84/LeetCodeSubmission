class Solution:
    def largestOddNumber(self, num: str) -> str:
        num=num[::-1]
        result=""
        for i in range(len(num)):
            if int(num[i])%2==1:
                result=num[i:]
                break
        result=result[::-1]
        return result
        
            