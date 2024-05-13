class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx=0
        flag=False
        result=word
        for letter in word:
            idx+=1
            if letter==ch:
                flag=True
                break
        if flag:
            result=word[0:idx][::-1]+word[idx:]
        return result
        