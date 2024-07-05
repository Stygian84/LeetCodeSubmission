class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        
        res=""
        flag=None
        for digit in num:
            digit=int(digit)
            replacement=change[digit]
            if replacement==digit:
                res+=str(digit)
                continue
            if (flag==None or flag==True) and replacement >= digit:
                res+=str(replacement)
                flag=True
            else:
                if flag==True:
                    flag=False
                res+=str(digit)
        return res
        '''
        "214010"
        [6,7,9,7,4,0,3,4,4,7]'''