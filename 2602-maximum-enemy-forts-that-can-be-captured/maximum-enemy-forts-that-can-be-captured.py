class Solution:
    def captureForts(self, forts: List[int]) -> int:
        #1 meet 1 reset
        #1 meet -1 or -1 meet 1, count total
        
        prev = forts[0]

        count = 0
        total = 0
        for item in forts[1:]:
            if prev==1 and item==1:
                count = 0

            elif (prev==1 and item==-1) or (prev==-1 and item==1):
                total = max(total,count)
                count=0
            
            if (item==1) or (item==-1):
                prev=item
                count=0
            
            else:
                count+=1
        return total


