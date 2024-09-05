class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        
        temp = deque([])
        n = len(skills)
        if k>n:
            return skills.index(max(skills))
        
        for i in range(n):
            temp.append((skills[i],i,0))

        while temp:
            a,b,c = temp.popleft()
            d,e,f = temp.popleft()

            if a>d:
                c+=1
                temp.appendleft((a,b,c))
                temp.append((d,e,f))
            else:
                f+=1
                temp.appendleft((d,e,f))
                temp.append((a,b,c))
            
            if c==k:
                return b
            if f==k:
                return e