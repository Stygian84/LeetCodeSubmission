class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq = defaultdict(int)

        for word in words2:
            c = Counter(word)
            for k,v in c.items():
                if k in freq:
                    freq[k] = max(freq[k],v)
                else:
                    freq[k] = v
                    

        res = []

        for word in words1:
            freq2 = Counter(word)
            valid = True
            for k,v in freq.items():
                if k in freq2 and freq2[k]>=v:
                    continue
                else:
                    valid = False
                    break
            if valid:
                res.append(word)
        
        return res