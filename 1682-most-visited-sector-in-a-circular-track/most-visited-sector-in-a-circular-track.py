class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        dc={}
        for i in range(1,len(rounds)):
            if rounds[i-1]>rounds[i]:
                for j in range(rounds[i-1],n+1):
                    dc[j]=dc.get(j,0)+1
                for j in range(1,rounds[i]):
                    dc[j]=dc.get(j,0)+1
            else:
                for j in range(rounds[i-1],rounds[i]):
                    dc[j]=dc.get(j,0)+1
        dc[rounds[-1]]=dc.get(rounds[-1],0)+1
        print(dc)
        res=[]
        max_value=max(dc.values())
        for key,values in dc.items():
            if values==max_value:
                res.append(key)
        res.sort()
        return res


        