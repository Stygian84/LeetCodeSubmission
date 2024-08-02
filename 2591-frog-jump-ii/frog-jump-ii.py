class Solution:
    def maxJump(self, stones: List[int]) -> int:
        
        n = len(stones)
        if n==2:
            return stones[1]-stones[0]

        cost = 0
        prev = stones[0]
        for i in range(0,n,2):
            cost = max(cost,stones[i]-prev)
            prev = stones[i]

        #back
        if n%2==1:
            n-=1
        for j in range (n-1,-1,-2):
            cost = max(cost,prev-stones[j])
            prev = stones[j]

        return cost