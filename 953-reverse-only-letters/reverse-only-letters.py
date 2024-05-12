class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ls=[]
        for letter in s:
            if letter.isalpha():
                ls.append(letter)
        ls.reverse()
        result=[]
        count=0
        for idx in range(len(s)):
            if s[idx].isalpha():
                result.append(ls[count])
                count+=1
            else:
                result.append(s[idx])
        return "".join(result)
        