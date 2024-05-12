class Solution:
    def freqAlphabets(self, s: str) -> str:
        dc={}
        for i in range(9):
            dc[str(i+1)]=chr(97+i)
        for i in range(17):
            dc[str(10+i)+"#"]=chr(106+i)
        ls=[]
        count=0
        for i in range(len(s)):
            if count>0:
                ls.append(s[i])
                count-=1
                continue
            if s[i]=="#":
                count=2
                ls.pop()
                ls.pop()
                ls.append(s[i-2]+s[i-1]+s[i])
                continue
            ls.append(s[i])
        print(ls)
        result=""
        for item in ls:
            result+=dc[item]
        return result
        