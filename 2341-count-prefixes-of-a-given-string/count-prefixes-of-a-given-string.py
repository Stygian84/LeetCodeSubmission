class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        def isSubstring(s,substring):
            prefix = ''
            idx=0
            for i in range(len(s)):
                if idx<=len(substring)-1 and s[i]==substring[idx]:
                    idx+=1
                    if idx==len(substring):
                        return True
                else:
                    return False
        count=0
        for word in words:
            if isSubstring(s,word):
                count+=1
        return count
        