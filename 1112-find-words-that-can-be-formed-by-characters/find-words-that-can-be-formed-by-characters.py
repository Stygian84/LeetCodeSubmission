class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dc={}
        for item in chars:
            dc[item]=dc.get(item,0)+1

        total=0
        for word in words:
            dc2=copy.copy(dc)
            for letter in word:
                if dc2.get(letter,0)==0:
                    break
                else:
                    dc2[letter]-=1
            else:
                total+=len(word)
        return total