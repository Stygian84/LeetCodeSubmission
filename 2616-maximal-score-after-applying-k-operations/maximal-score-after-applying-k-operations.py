class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        ls=[]
        for num in nums:
            heapq.heappush(ls,-num)

        score=0

        for _ in range(k):
            value = -heapq.heappop(ls)
            score += value
            value = math.ceil(value/3)
            heapq.heappush(ls,-value)

        return score