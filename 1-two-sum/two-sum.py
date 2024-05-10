class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ls = []
        for idx in range(0, len(nums)):
            new_num = target - nums[idx]
            if new_num in nums[idx + 1 :]:
                ls.append(idx)
                ls.append(nums[idx + 1 :].index(new_num) + idx + 1)
                return ls
            else:
                continue
