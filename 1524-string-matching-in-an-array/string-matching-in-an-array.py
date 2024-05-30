class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for word in words:
            for check in words:
                if len(word)>len(check):
                    continue
                if word!=check and word in check:
                    res.append(word)
                    break
        return res