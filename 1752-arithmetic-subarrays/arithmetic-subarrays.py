class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def canMakeArithmeticProgression(arr: List[int]) -> bool: #from 1502
            arr.sort()
            diff=arr[1]-arr[0]
            for idx in range(1,len(arr)-1):
                if arr[idx+1]-arr[idx]==diff:
                    continue
                else:
                    return False
            return True

        result=[]
        for idx in range(len(l)):
            left=l[idx]
            right=r[idx]+1
            result.append(canMakeArithmeticProgression(nums[left:right]))
            
        return result
        