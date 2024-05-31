class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words)==1:
            return []
        res=[]
        for letter in words[0]:
            check=True
            count=words[0].count(letter)
            min_count=words[0].count(letter)
            for idx in range(1,len(words)):
                if letter not in words[idx]:
                    check=False
                    break
                else:
                    if words[idx].count(letter)!=count:
                        if words[idx].count(letter)<min_count:
                            min_count=words[idx].count(letter)
            if check and letter not in res:
                for _ in range(min_count):
                    res.append(letter)
                    continue
        return res