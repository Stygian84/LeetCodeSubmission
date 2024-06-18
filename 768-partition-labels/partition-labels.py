class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dc=defaultdict(list)
        for i in range(len(s)):
            letter=s[i]
            if letter not in dc:
                dc[letter]=[i,-1]
            else:
                dc[letter][1]=i
        low=math.inf
        high=-math.inf
        res=[]
        for value in dc.values():
            
            first=value[0]
            second=value[1]
            
            if high<first:
                print(high,low)
                if high==-1:
                    res.append(1)
                else:                
                    res.append(high-low+1)
                low=math.inf
                high=-math.inf
            low=min(low,first)
            high=max(high,second)
        if high==-1:
            res.append(1)
        else:               
            res.append(high-low+1)
        res=res[1:]
        return res
