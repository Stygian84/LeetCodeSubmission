class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        def isBeautiful(x):
            if not x:
                return False
            if x[0]=="0":
                return False
            value = int(x,2)
            while value%5==0 and value>1:
                value/=5
            return value==1

        res=math.inf
        def all_partitions(s):
            if not s:
                return [[]] 
            
            partitions = []
            for i in range(1, len(s) + 1):
                if s[i:] and s[i:][0]=="0":
                    continue
                for partition in all_partitions(s[i:]):
                    partitions.append([s[:i]] + partition)
            return partitions
        partitions = all_partitions(s)

        for p in partitions:
            for item in p:
                if not isBeautiful(item):
                    break
            else:
                res=min(res,len(p))

        if res==math.inf:
            return -1
        return res