class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def transform(word):
            result=""
            for letter in word:
                result+=str(ord(letter)-ord('a'))
            return int(result)
        return transform(firstWord)+transform(secondWord)==transform(targetWord)
        
        