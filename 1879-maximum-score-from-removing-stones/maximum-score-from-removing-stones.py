class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        ls=[-a,-b,-c] #maxheap
        heapq.heapify(ls)
        count=0
        while len(ls)>1:
            count+=1

            maximum = -heapq.heappop(ls) - 1
            maximum2 = -heapq.heappop(ls) - 1
            if maximum2!=0:
                heapq.heappush(ls,-maximum2)
            if maximum!=0:
                heapq.heappush(ls,-maximum)
                
        return count

