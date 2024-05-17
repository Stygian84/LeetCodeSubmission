class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        if not word.isalnum():
            return False
        vowel=False
        consonant=False
        for item in word:
            if item.isalpha():
                if item in "aeiouAEIOU":
                    vowel=True
                else:
                    consonant=True
        if vowel and consonant:
            return True
        else:
            return False    