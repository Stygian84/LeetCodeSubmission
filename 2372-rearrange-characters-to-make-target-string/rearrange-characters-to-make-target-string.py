class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        if len(target)>len(s):
            return 0

        freq = Counter(s)
        freq_target = Counter(target)
        
        count = math.inf
        
            
        for letter in target:
            a=freq_target[letter]
            if letter in freq:
                b=freq[letter]
            else:
                return 0
            count = min(count,b//a)
        return count