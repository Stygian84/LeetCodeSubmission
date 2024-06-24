class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
            max_length=-1


            for i in range(len(nums)-1):

                length=1
                flag=True

                for j in range(i,len(nums)-1):
                    if flag and nums[j+1]==nums[j]+1:
                        flag=False
                        length+=1
                    elif not flag and nums[j+1]==nums[j]-1:
                        flag=True
                        length+=1
                    else:
                        break
                    if length>max_length:
                        max_length=length

            if max_length>=2:
                return max_length
                
            return -1