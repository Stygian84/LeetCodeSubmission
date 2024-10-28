class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # check if upper is the same, then continue till pattern[j+1]is upper
        res = []
        n = len(pattern)
        for word in queries:
            
            j = 0
            flag = True
            for i in range(len(word)):
                if j<len(pattern) and word[i]==pattern[j]:
                    j+=1
                else:
                    if j<len(pattern) and word[i].islower() and pattern[j].isupper():
                        continue
                    if word[i].isupper():
                        flag = False
                                    
            if flag and (i==len(word) or j==len(pattern)):
                res.append(True)
            else:
                res.append(False)
        return res
                    