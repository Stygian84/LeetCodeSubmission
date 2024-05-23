class Solution:
    def isValid(self, s: str) -> bool:
        ls=[]
        if len(s)<=1:
            return False
        dc={")":"(","]":"[","}":"{"}
        for item in s:
            if item in dc.keys():
                if ls and ls[-1]==dc[item]:
                    ls.pop() 
                else:
                    ls.append(item)               
            else:
                ls.append(item)
        if ls == []:
            return True
        else:
            return False 
        
        