class Solution:
    def reorderSpaces(self, text: str) -> str:
        num_space=0
        ls=text.split()
        division=max(len(ls)-1,1)
        for item in text:
            if item==" ":
                num_space+=1

        res=""
        for item in ls:
            res+=item
            res+=" "*(num_space//division)
        if len(ls)>1:
            res=res.rstrip()
        res+=" "*(num_space%division)
        return res