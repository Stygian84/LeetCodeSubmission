class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        value_needed=math.inf
        idx=0
        for item in numbers:
            value_needed=target-item
            if value_needed in numbers:
                break
            idx+=1
        return [idx+1,len(numbers) - 1 - numbers[::-1].index(value_needed)+1]        