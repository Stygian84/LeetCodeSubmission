class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        ls=[a,b,c]
        ls.sort()

        total = ls[0]+ls[1]
        if total > ls[-1]:
            return ls[-1] + (total-ls[-1]) //2
        return total
        '''ls=[-a,-b,-c] #maxheap
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
                
        return count'''

