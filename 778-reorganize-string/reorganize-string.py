class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = Counter(s)

        max_heap = []
        for key,value in freq.items():
            heapq.heappush(max_heap, (-value,key) )

        res = []
        prev_count,prev_char = 0 , ""
        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)
            
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            prev_count, prev_char = count + 1, char  
        
        if len(res)!=len(s):
            return ""
        return ''.join(res)
        
        '''dc={}
        for letter in s:
            dc[letter]=dc.get(letter,0)+1
        res=""
        prev_values = None
        while True:
            current_values = list(dc.values())
            print(current_values)
            if prev_values is not None and current_values == prev_values:
                if any(value != 0 for value in current_values):
                    return ""
                break
            prev_values = current_values
            for key, values in sorted(dc.items(), key=lambda x: x[1], reverse=True):
                if res=="":
                    res+=key
                    dc[key]-=1
                    continue
                if values>0 and res[-1]!=key:
                    res+=key
                    dc[key]-=1
            print(res)
        return res
        '''