class Solution:
    def validStrings(self, n: int) -> List[str]:
        res=[]

        def generate(current,length):
            if length==n:
                res.append(current)
                return
            
            if current[-1]=="1":
                generate(current+"0",length+1)
                generate(current+"1",length+1)
            else:
                generate(current+"1",length+1)
            
        generate("0",1)
        generate("1",1)
        return res