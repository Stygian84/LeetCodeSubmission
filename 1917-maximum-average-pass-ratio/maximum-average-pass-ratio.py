class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap=[]
        one_count=0
        for s,t in classes:
            if s==t:
                one_count+=1
                continue
            improvement = (s + 1) / (t + 1) - s / t
            heapq.heappush(max_heap, (-improvement, s, t))
        

        for _ in range(extraStudents):
            if not max_heap:
                break
            improvement, s, t = heapq.heappop(max_heap)
            s += 1
            t += 1
            new_improvement = (s + 1) / (t + 1) - s / t
            heapq.heappush(max_heap, (-new_improvement, s, t))
        
        total=one_count
        for a,b,c in max_heap:
            total+=b/c
            
        return total/len(classes)