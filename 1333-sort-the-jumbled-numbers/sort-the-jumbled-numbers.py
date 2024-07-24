class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        s = []
        dc = {}
        for i in range(len(mapping)):
            dc[i]=mapping[i]

        for i in range(len(nums)):
            #s.append((nums[i],i))
            temp=[]
            for digit in str(nums[i]):
                temp.append(dc[int(digit)])
            res=0
            for digit in temp:
                res = res*10+digit
            s.append((res,i))

        s.sort()

        result = []
        for _,idx in s:
            result.append(nums[idx])
        return result

        
