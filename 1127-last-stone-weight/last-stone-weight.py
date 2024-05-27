
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [] 
        for item in stones:
            heapq.heappush(max_heap, -item)

        while len(max_heap)>1:
            y=-heapq.heappop(max_heap)
            x=-heapq.heappop(max_heap)
            if y!=x:
                heapq.heappush(max_heap, x-y)
        if len(max_heap)==0:
            return 0
        return -max_heap[0]

        '''
        stones.sort()
        while len(stones)>1:
            print(stones)
            stones.sort()
            y=stones[-1]
            x=stones[-2]
            stones=stones[:-2]
            if y!=x:
                stones.append(abs(y-x))
        if len(stones)==0:
            return 0
        return stones[0]
        '''