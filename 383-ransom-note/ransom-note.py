class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag={}
        for letter in magazine:
            mag[letter]=mag.get(letter,0)+1
        for letter in ransomNote:
            if letter in mag:
                mag[letter]-=1
                if mag[letter]<0:
                    return False

            else:
                return False
        if any(value<0 for value in mag.values()):
            return False
        return True