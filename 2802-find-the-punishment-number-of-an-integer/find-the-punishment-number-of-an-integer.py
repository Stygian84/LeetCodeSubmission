class Solution:
    def punishmentNumber(self, n: int) -> int:
        def all_partitions(s):  
            if not s:
                return [[]]          
            partitions = []
            for i in range(1, len(s) + 1):
                prefix = s[:i]
                for partition in all_partitions(s[i:]):
                    partitions.append([prefix] + partition)
            return partitions

        def check(x):
            str_x=str(x*x)
            partitions = all_partitions(str_x)
            for item in partitions:
                temp=0
                for digit in item:
                    temp+=int(digit)
                if temp==x:
                    return True
            return False

        total=0
        for i in range(1,n+1):
            if i%9==1 or i%9==0:
                if check(i):
                    total+=i*i
        return total