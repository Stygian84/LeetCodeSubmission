class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        dc = {}
        for i in range(len(change)):
            dc[str(i)] = str(change[i])
        
        res=""
        flag=None
        for digit in num:
            if dc[digit]==digit:
                res+=digit
                continue
            if (flag==None or flag==True) and dc[digit] >= digit:
                res+=dc[digit]
                flag=True
            else:
                if flag==True:
                    flag=False
                res+=digit
        return res
        '''
        "214010"
        [6,7,9,7,4,0,3,4,4,7]'''