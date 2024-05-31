class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        dc={}
        for idx in range(len(nums)-1):
            if nums[idx]==key:
                dc[nums[idx+1]]=dc.get(nums[idx+1],0)+1
        max_key=-1
        max_value=-1
        for keys,values in dc.items():
            if values>max_value:
                max_value=values
                max_key=keys
        return max_key