class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        #can only take front or behind
        #must take at least k of each 'a' 'b' 'c'
        frequency = Counter(s)
        for letter in 'abc':
            if frequency[letter] < k :
                return -1
        

        
        res = deque([])
        total = 0

        n = len(s)
        for i in range(n):
            res.append(s[i])
            frequency[s[i]]-=1
            while res and frequency[s[i]]<k:
                removed = res.popleft()
                frequency[removed]+=1
            total = max(total,len(res))

        return n-total    