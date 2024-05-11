class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counter=-1
        counter=0
        for item in nums:
            if item!=1:
                if counter>max_counter:
                    max_counter=counter
                counter=0
            else:
                counter+=1
        
        if counter>max_counter:
            max_counter=counter
        return max_counter
        