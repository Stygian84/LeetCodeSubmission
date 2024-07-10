class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        total/=3
        temp_total = 0
        count = 0

        for num in arr:
            temp_total+=num
            if temp_total == total:
                count+=1
                temp_total=0
                  
        if total<=0:
            return count >= 3
        return count == 3