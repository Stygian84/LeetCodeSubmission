class Solution:
    def reformat(self, s: str) -> str:
        digit=[]
        alpha=[]
        for letter in s:
            if letter.isalpha():
                alpha.append(letter)
            else:
                digit.append(letter)
        
        res=""
        while digit and alpha:
            res+=digit.pop()
            res+=alpha.pop()
            
        if digit:
            if len(res)==0 or res[-1].isalpha():
                res+=digit.pop()
            elif res[0].isalpha():
                res=digit.pop()+res
        
        if alpha:
            if len(res)==0 or res[-1].isnumeric():
                res+=alpha.pop()
            elif res[0].isnumeric():
                res= alpha.pop() + res
        
        if alpha or digit:
            return ""
        else:
            return res