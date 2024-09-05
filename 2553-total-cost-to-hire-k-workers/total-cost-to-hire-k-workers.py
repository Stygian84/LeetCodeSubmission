class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        total = 0

        first = []
        last = []

        for i in range(candidates):
            heapq.heappush(first,(costs[i]))
        
        for j in range(max(n-candidates,candidates),n):
            heapq.heappush(last,(costs[j]))
        
        i=candidates
        j=n-candidates-1

        total = 0
        for _ in range(k):
            if not last or (first and first[0]<=last[0]):
                cost = heapq.heappop(first)
                total+=cost

                if i<=j:
                    heapq.heappush(first,(costs[i]))
                    i+=1

            else:
                cost = heapq.heappop(last)
                total+=cost

                if i<=j:
                    heapq.heappush(last,(costs[j]))
                    j-=1
        return total