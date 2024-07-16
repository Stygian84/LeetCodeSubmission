class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dc=defaultdict(list)

        def totalDigits(x):
            total=0
            while x>0:
                digit = x%10
                total+=digit
                x//=10
            return total

        largest_sum=-1

        for num in nums:
            total=totalDigits(num)
            if total in dc:
                last=dc[total][-1]
                if num>=last:
                    dc[total].append(num)
                
                if last+num>largest_sum:
                    largest_sum=last+num
                    
            else:
                dc[total].append(num)


        return largest_sum