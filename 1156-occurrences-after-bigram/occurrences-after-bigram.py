class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        ls=text.split()

        if len(ls)<=2:
            return []

        res=[]

        q = deque([ls[0],ls[1]])

        for i in range(2,len(ls)):
            q.append(ls[i])
            if q[0]==first:
                if q[1]==second:
                    res.append(q[-1])

            q.popleft()

        return res