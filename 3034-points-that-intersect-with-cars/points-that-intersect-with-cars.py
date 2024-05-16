class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        result=set()
        for item in nums:
            for i in range(item[0],item[1]+1):
                result.add(i)
        return len(result)
        