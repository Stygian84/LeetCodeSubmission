class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()
        res=[]
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])

        min_len = min(len(odd), len(even))
        if len(odd) > min_len:
            res.extend(odd[min_len:])
        elif len(even) > min_len:
            res.extend(even[min_len:])
            
        return res