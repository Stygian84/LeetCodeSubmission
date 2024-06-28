class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dc=defaultdict(int)

        for letter in licensePlate:
            if letter.isalpha():
                dc[letter.lower()]+=1


        res=""
        length=math.inf
        
        for word in words:
            if len(word)>=length:
                continue

            dc2=copy.copy(dc)
            for letter in word:
                if letter in dc2:
                    dc2[letter]-=1
            
            if all(value<=0 for value in dc2.values()):
                res=word
                length=len(word)

        return res