class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        q = deque([])
        freq = Counter(p)
        count = defaultdict(int)
        seen = set(p)
        res = []

        n = len(s)
        m = len(p)

        for i in range(n):
            if len(q)==m: #check
                if count==freq:
                    res.append(i-m)
                removed = q.popleft()
                count[removed]-=1

            # if letter in p
            if s[i] in seen:
                q.append(s[i])
                count[s[i]] += 1
            else:
                q = deque([])
                count = defaultdict(int)
                

        if len(q)==m: #check
            if count==freq:
                res.append(i-m+1)
                
        return res
        '''queue = deque([])
        freq = Counter(p)

        res = []
        count = defaultdict(int)

        for i in range(len(s)):
            if s[i] in freq:
                queue.append(s[i])
                count[s[i]]+=1
                if count == freq:
                    res.append(i-len(queue)+1)
                    count[queue.popleft()]-=1
            else:
                while count and queue and count!=freq:
                    removed = queue.popleft()
                    count[removed]-=1
                if count==freq:
                    res.append(i-len(queue))
        
        return res'''