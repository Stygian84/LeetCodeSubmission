class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        res=[]
        for word in words:

            dc={}
            mapped_values=set()

            for w,p in zip(word,pattern):
                if p not in dc:
                    if w in mapped_values:
                        break
                    dc[p]=w
                    mapped_values.add(w)
                else:
                    if dc[p]!=w:
                        break

            else:
                res.append(word)

        return res