class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        prefix=[]
        for a,b in zip(s,t):
            diff=abs(ord(a)-ord(b))
            prefix.append(diff)
        print(prefix)
        
        max_length=0
        total=0
        current=deque([])
        
        for i in range(len(prefix)):
            total += prefix[i]
            current.append(prefix[i])
            
            while total > maxCost:
                total -= current.popleft()
            
            max_length = max(max_length, len(current))
        return max_length
