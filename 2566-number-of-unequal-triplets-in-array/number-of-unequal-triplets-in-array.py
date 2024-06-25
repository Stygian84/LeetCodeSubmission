class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:


        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1

        total_triplets = 0
        prefix_count = 0
        total_elements = len(nums)
        
        
        for num in count_map:
            suffix_count = total_elements - prefix_count - count_map[num]
            total_triplets += prefix_count * count_map[num] * suffix_count
            prefix_count += count_map[num]
        return total_triplets
        '''if len(set(nums))<=2:
            return 0
        
        count=0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]!=nums[j] and nums[j]!=nums[k] and nums[i]!=nums[k]:
                        count+=1
        
        return count'''