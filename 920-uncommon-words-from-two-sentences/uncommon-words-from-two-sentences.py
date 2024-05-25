class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res=[]
        ls1=s1.split()
        ls2=s2.split()
        for item in ls1:
            if ls1.count(item)==1 and ls2.count(item)==0:
                res.append(item)      
        
        for item in ls2:
            if ls2.count(item)==1 and ls1.count(item)==0:
                res.append(item)   
        return res