class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels="aeiou"
        ls=sentence.split()
        for idx in range(len(ls)):
            if ls[idx][0].lower() in vowels:
                pass
            else:
                ls[idx]=ls[idx][1:]+ls[idx][0]
            ls[idx]+="ma"
            ls[idx]+="a"*(idx+1)
        return " ".join(ls)