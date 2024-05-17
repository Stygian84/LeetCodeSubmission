class Solution:
    def minimumPushes(self, word: str) -> int:
        dc={}
        for letter in word:
            dc[letter]=dc.get(letter,0)+1
        values=[]
        for value in dc.values():
            values.append(value)
        values.sort(reverse=True)
        counter=0
        result=0
        for idx in range(len(values)):
            if idx!=0 and idx%8==0:
                counter+=1
            result+=values[idx]+counter
        return result