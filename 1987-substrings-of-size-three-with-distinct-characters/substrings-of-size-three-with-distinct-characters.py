class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0
        count=0
        current=deque(s[:3])
        if len(set(current))==3:
            count+=1
        for letter in s[3:]:
            current.popleft()
            current.append(letter)
            if len(set(current))==3:
                count+=1
        return count
