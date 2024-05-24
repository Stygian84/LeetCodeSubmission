class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ls=[]
        temp=""
        for item in num:
            if temp=="":
                temp+=item
                continue
            if item in temp:
                temp+=item
                if len(temp)==3:
                    ls.append(int(temp))
                    temp=""
                    continue
            else:
                temp=item
        if ls:
            return str(max(ls)).zfill(3)
        else:
            return ""