class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        minimum=min(len(s3),len(s2),len(s1))
        count=0
        for i in range(minimum):
            if s1[i]==s2[i]==s3[i]:
                count+=1
                continue
            else:
                break
        if count==0:
            return -1
        return len(s3)+len(s2)+len(s1)-count*3
        
    