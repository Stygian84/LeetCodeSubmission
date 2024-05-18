class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        dc={}
        length = len(bin(max(nums)))-2
        for item in nums:
            for i in range(length):
                binary=bin(item)[2:].zfill(length)
                if binary[i]=="1":
                    dc[i]=dc.get(i,0)+1
                else:
                    dc[i]=dc.get(i,0)
        result=""
        for key,values in dc.items():
            if values>=k:
                result+="1"
            else:
                result+="0"
        return int(result,2)