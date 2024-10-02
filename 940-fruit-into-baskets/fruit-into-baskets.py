class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        queue = deque([])
        freq = defaultdict(int)
        maximum = 0
        for fruit in fruits:
            queue.append(fruit)
            freq[fruit]+=1
            
            while len(freq)>2:
                removed = queue.popleft()
                freq[removed]-=1
                if freq[removed]==0:
                    del freq[removed]
            
            maximum = max(maximum,len(queue))
            
        return maximum