class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(a,b):
            if a+b>b+a:
                return -1
            else:
                return 1

        str_list=[]
        for num in nums:
            str_list.append(str(num))
        str_list.sort(key=cmp_to_key(compare))
        
        res = "".join(str_list)

        if int(res)==0:
            return "0"

        return res