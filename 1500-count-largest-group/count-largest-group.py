class Solution:
    def countLargestGroup(self, n: int) -> int:
        dc=defaultdict(list)
        for i in range(1,n+1):
            total=0
            for digit in str(i):
                total+=int(digit)
            dc[total]+=[i]
        
        max_length=0
        count=0
        for key,value in dc.items():
            if len(value)>max_length:
                count=0
                max_length=len(value)
            if len(value)==max_length:
                count+=1
        return count