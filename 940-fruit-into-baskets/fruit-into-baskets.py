class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        left = 0
        maximum = 0

        for right in range(len(fruits)):
            freq[fruits[right]] += 1

            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1

            maximum = max(maximum, right - left + 1)

        return maximum
        '''queue = deque([])
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

        return maximum'''