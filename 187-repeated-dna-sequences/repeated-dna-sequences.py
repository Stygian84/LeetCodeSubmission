class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        max_length=10
        dna={}
        current=""
        for item in s:
            if len(current)==max_length:
                dna[current]=dna.get(current,0)+1
                current=current[1:]
            current+=item
        if len(current)==max_length:
            dna[current]=dna.get(current,0)+1
        
        res=[]
        for key,values in dna.items():
            if values>1:
                res.append(key)    
        return res