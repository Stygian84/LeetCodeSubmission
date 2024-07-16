class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums3=[]
        for a,b in zip(nums1,nums2):
            nums3.append([b,a])
        
        nums3.sort(reverse=True)
        min_heap = []
        current_sum = 0
        max_score = 0
        
        for b, a in nums3:
            heapq.heappush(min_heap, a)
            current_sum += a
            
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
                
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * b)
        
        return max_score