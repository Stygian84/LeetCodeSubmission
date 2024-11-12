class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #make window with size n with at most k different charcter
        
        n = len(s)
        freq = defaultdict(int)
        queue = deque([])
        res = 0


        for i in range(n):
            freq[s[i]] += 1
            queue.append(s[i])    
            
            while len(queue)-max(freq.values())>k:
                removed = queue.popleft()
                freq[removed]-=1
            res = max(res,len(queue))

        return res

        '''if len(set(s))==1:
            return len(s)
        queue = deque([])
        freq = defaultdict(int)
        maximum = 0

        for i in range(len(s)):
            queue.append(s[i])

            freq[s[i]]+=1
            while len(freq)>k and min(freq.values())>k:
                removed = queue.popleft()
                freq[removed]-=1
            maximum = max(maximum,len(queue))

        return maximum
        '''
        '''i=0
        j=1
        n = len(s)
        #keep track of different letter
        queue = deque([])
        count=0
        res = 0
        for i in range(n):
            queue.append(s[i])
            if s[i]!=queue[-1]:
                count+=1
            if count==k:
                res = max(res,len(queue))
        return res'''