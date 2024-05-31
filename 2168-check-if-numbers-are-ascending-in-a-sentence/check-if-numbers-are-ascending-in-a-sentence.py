class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        ls=s.split()
        res=[]
        for item in ls:
            if item.isdigit():
                if res==[]:
                    res.append(int(item))
                else:
                    if int(item)<=res[-1]:
                        return False
                    res.append(int(item))
        return True
                    
        