class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""
            
        n = len(encodedText)

        ls = []
        temp_ls = []
        for i in range(n):
            temp_ls.append(encodedText[i])
            if len(temp_ls)==n//rows:
                ls.append("".join(temp_ls))
                temp_ls=[]

        res = []
        i = 0
        j = 0
        step = 1
        while j<len(ls[0]):
            res.append(ls[i][j])
            i+=1
            j+=1
            if i>=len(ls):
                i=0
                j=0
                j+=step
                step+=1

        return "".join(res).rstrip()