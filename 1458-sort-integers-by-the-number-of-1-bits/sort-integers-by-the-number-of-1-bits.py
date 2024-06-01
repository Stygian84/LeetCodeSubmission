class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dc={}
        arr.sort()
        min_bit=math.inf
        max_bit=-1
        for item in arr:
            bits=bin(item)[2:].count("1")
            if bits>max_bit:
                max_bit=bits
            if bits<min_bit:
                min_bit=bits
            dc[bits]=dc.get(bits,[])+[item]

        res=[]
        for i in range(min_bit,max_bit+1):
            try:
                res.extend(dc[i])
            except:
                pass
        return res
        

        