class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_ls=[]
        text=[]
        vowel=['a','e','i','o','u']
        for letter in s:
            if letter.lower() in vowel:
                vowel_ls.append(letter)
                text.append(1)
            else:
                text.append(letter)
        result=""
        vowel_ls.reverse()
        idx=0
        for item in text:
            if item == 1:
                result+=vowel_ls[idx]
                idx+=1
            else:
                result+=item
        return result
        