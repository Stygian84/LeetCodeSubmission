class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        n = len(words)
        sets = []
        for word in words:
            sets.append(set(word))

        res = 0
        for i in range(n):
            for j in range(i+1,n):
                if not (sets[i] & sets[j]):
                    length = len(words[i])*len(words[j])
                    if length > res:
                        res = length
        
        return res