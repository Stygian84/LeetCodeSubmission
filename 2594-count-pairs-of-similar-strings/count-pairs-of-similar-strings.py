class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count=0
        dc=defaultdict(int)
        for word in words:
            s=list(set(word))
            s.sort()
            dc["".join(s)]+=1
            
        for key,values in dc.items():
            count+=(values-1)*values//2

        return count