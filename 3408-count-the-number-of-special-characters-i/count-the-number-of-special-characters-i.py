class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        ls=[]
        for item in word:
            if chr(ord(item)-32) in word and item not in ls:
                ls.append(item)
                count+=1
        return count
        