class Solution:
    def minFlips(self, target: str) -> int:
        count=0

        for bit in target:
            if (count%2==1 and bit=="0"): 
                count+=1
            elif(count%2==0 and bit=="1"):
                count+=1
        return count

            

