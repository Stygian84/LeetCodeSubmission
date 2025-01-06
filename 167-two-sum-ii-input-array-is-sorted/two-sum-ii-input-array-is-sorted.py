class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        dc = {}
        for i in range(len(numbers)):
            diff = target-numbers[i]
            if diff in dc:
                res.append(dc[diff]+1)
                res.append(i+1)
                return res
            dc[numbers[i]]=i
        
        return res