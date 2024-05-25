class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res=[]
        temp_str=""
        temp_ls=[]
        for idx in range(len(s)):
            print(temp_str)
            if temp_str=="":
                temp_str+=s[idx]
                temp_ls.append(idx)
                continue
            if s[idx] in temp_str:
                temp_str+=s[idx]
            else:
                if len(temp_str)>=3:
                    temp_ls.append(idx-1)
                    res.append(temp_ls)
                    temp_ls=[idx]
                temp_str=s[idx]
                temp_ls[0]=idx
        if len(temp_str)>=3:
            temp_ls.append(len(s)-1)
            res.append(temp_ls)
        
                
                
        return res
                    