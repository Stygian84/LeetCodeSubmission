class Solution:
    def sortVowels(self, s: str) -> str:
        ls=[]
        vowels="aeiouAEIOU"
        res=[]
        for item in s:
            res.append(item)
            if item in vowels:
                ls.append(item)
            
        ls.sort()
        idx=0
        for i in range(len(res)):
            if res[i] in vowels:
                res[i]=ls[idx]
                idx+=1
        return "".join(res)