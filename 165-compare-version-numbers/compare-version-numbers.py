class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ls1=version1.split(".")
        ls2=version2.split(".")

        n=max(len(ls1),len(ls2))
        
        for i in range(n):
            value1,value2=0,0            

            if i<len(ls1):
                value1=int(ls1[i])
            if i<len(ls2):
                value2=int(ls2[i])
            if value1<value2:
                return -1
            elif value1>value2:
                return 1

        return 0