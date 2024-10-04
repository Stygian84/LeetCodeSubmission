class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def convert(time):
            hour = int(time[:2])
            minutes = int(time[3:])
            return hour*60+minutes
        
        freq = defaultdict(list)
        for name,time in zip(keyName,keyTime):
            freq[name].append(convert(time))
        #print(freq)
        
        res = []
        for k,v in freq.items():
            if len(v)<3:
                continue
            sorted_time = sorted(v)
            for i in range(1,len(v)-1):
                if 0<sorted_time[i+1]-sorted_time[i-1]<=60 :
                    res.append(k)
                    break
        res.sort()
        return res