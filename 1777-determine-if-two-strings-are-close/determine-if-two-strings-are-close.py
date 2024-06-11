class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        dc1={}
        dc2={}
        for a,b in zip(word1,word2):
            dc1[a]=dc1.get(a,0)+1
            dc2[b]=dc2.get(b,0)+1
        
        if set(dc1.keys()) != set(dc2.keys()):
            return False

        if sorted(dc1.values()) != sorted(dc2.values()):
            return False

        return True
