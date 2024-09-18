class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        for k,v in freq.items():
            if v>=3:
                if v%2==1:
                    freq[k] = 1
                else:
                    freq[k] = 2
        
        return sum(freq.values())