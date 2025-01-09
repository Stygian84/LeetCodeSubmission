class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n=len(pref)
        count=0
        for item in words:
            if item[:n]==pref:
                count+=1
        return count