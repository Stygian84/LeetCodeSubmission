class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''def computePrefixSum(arr):
            prefix_sum=[0]*len(arr)
            prefix_sum[0]=arr[0]
            for i in range(1,len(arr)):
                prefix_sum[i]=prefix_sum[i-1]+arr[i]
            return prefix_sum
        def range_sum(l,r,arr):
            if l==0:
                return arr[r]
            else:
                return arr[r]-arr[l-1]

        prefix_sum=computePrefixSum(nums)'''
        count = 0
        prefix_sum = 0
        remainder_count = {0: 1}  
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
           
            if remainder < 0:
                remainder += k
            
            if remainder in remainder_count:
                count += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1
        
        return count
