import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        heap = nums[:k]

        for num in nums[k:]:
            if num > heap[0]: 
                heapq.heappushpop(heap, num)
        return heap[0]