class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ls=text.split()
        count=0
        for item in ls:
            skip=False
            for letter in brokenLetters:
                if letter in item:
                    skip=True
                    break
            if skip:
                continue
            else:
                count+=1
        return count