class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        if k==len(reward1):
            return sum(reward1)
        ls=[]

        for a,b in zip(reward1,reward2):
            ls.append( (b-a,a,b))

        heapq.heapify(ls)
        res=0

        while ls:
            val = heapq.heappop(ls)
            if k>0:
                res+=val[1]
            else:
                res+=val[2]
            k-=1
        
        return res