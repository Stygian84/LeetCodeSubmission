class Solution:
    def equalFrequency(self, word: str) -> bool:
        dc = Counter(word)
        freq = Counter(dc.values())
        
        if len(freq) == 1:
            if dc[word[0]]==1:
                return True
            if len(dc)==1:
                return True
            return False
        if len(freq) == 2:
            f1, f2 = freq.keys()
            if abs(f1 - f2) == 1:
                if freq[f1] == 1 and (f1 - 1 == 0 or f1 - 1 == f2):
                    return True
                if freq[f2] == 1 and (f2 - 1 == 0 or f2 - 1 == f1):
                    return True
            if 1 in freq and freq[1] == 1:
                return True
        
        return False