class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel="aeiou"
        res=0

        for item in words[left:right+1]:
            if item[0] in vowel and item[-1] in vowel:
                res+=1
        return res