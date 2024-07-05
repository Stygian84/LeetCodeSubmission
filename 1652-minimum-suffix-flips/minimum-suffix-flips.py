class Solution:
    def minFlips(self, target: str) -> int:
        n=len(target)
        count=0

        for i in range(n):
            if (count%2==1 and target[i]=="0") or (count%2==0 and target[i]=="1"):
                count+=1
        return count

            

