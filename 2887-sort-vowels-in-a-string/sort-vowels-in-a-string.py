class Solution:
    def sortVowels(self, s: str) -> str:
        ls=[]
        vowels="aeiouAEIOU"
        for item in s:
            if item in vowels:
                ls.append(item)
        ls.sort()
        res=""

        for item in s:
            if item in vowels:
                res+=ls.pop(0)
            else:
                res+=item

        return res