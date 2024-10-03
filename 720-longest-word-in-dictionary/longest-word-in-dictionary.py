class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort(key  = lambda x:len(x))
        seen = set()
        length = 0
        result = ""
        for word in words:
            if len(word)==1:
                if len(word)>length:
                    length = len(word)
                    result=word
                if len(word)==length:
                    if word<result:
                        result=word
                seen.add(word)

            else:
                if word[:-1] in seen:
                    seen.add(word)
                    if len(word)>length:
                        length = len(word)
                        result=word

                    elif len(word)==length:
                        if word<result:
                            result=word
                    

        return result