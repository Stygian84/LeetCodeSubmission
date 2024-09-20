class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        res = []
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                res.append(num)
                if len(res)==2:
                    return res