class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        n = len(nums)
        result = []
        dq = deque()

        for i in range(n):
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

        '''window=deque([])
        n=len(nums)

        maximum=[]
        max_heap=[]

        for i in range(n):
            window.append(-nums[i])
            heapq.heappush(max_heap,-nums[i])
            
            if len(window)==k:
                removed = window.popleft()

                maximum.append(-max_heap[0])

                if removed==max_heap[0]:
                    heapq.heappop(max_heap)
                    continue
                max_heap.remove(removed)
                heapq.heapify(max_heap)

            
        

        return maximum'''