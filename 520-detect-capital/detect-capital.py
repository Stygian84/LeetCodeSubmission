class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper()==word:
            return True
        if word.lower()==word:
            return True
        if word.title()==word:
            return True
        return False


