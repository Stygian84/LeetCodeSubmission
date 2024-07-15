class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res=""
        total=0
        count=0
        # a = 1,z=26
        # 1 1 x 26 26 = 73-54 = 19
        # 72 71 52 78
        while n-count>1 and 26*(n-count-1)>=k-total:
            res+="a"
            count+=1
            total+=1
        
        
        remaining = k-total
        
        count_z=remaining//26
        leftover = remaining - 26 * count_z
        if leftover > 0:
            res+=(chr(leftover + ord('a') - 1))
            
        res+="z"*count_z

        return res

