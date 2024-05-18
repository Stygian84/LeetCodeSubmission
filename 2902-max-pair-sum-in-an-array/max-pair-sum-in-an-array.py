class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def maximumDigit(num):
            max_num=-1
            for digit in str(num):
                if int(digit)>max_num:
                    max_num=int(digit)
            return max_num
        dc={}
        for number in nums:
            max_digit=maximumDigit(number)
            dc[max_digit]=dc.get(max_digit,[])+[number]
        result=-1
        for key,values in dc.items():
            if len(values)>=2:
                sorted_values=sorted(values)
                if sorted_values[-1]+sorted_values[-2] > result:
                    result=sorted_values[-1]+sorted_values[-2]
        return result