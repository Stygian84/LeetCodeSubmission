class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        dc={}
        for letter in allowed:
            dc[letter]=dc.get(letter,0)+1
        count=0
        for word in words:
            for letter in word:
                if dc.get(letter,0)==0:
                    break
                if word.count(letter)<dc.get(letter):
                    break
            else:
                count+=1
        return count