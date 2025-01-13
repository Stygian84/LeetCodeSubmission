class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        queue = deque()
        seen = set()

        for letter in s:
            while letter in seen:
                seen.remove(queue.popleft())
            
            queue.append(letter)
            seen.add(letter)
            length = max(length,len(queue))
        return length