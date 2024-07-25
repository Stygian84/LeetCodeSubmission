class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        diff=[]
        n = len(nums)
        for i in range(1,n):
            diff.append(nums[i]-nums[i-1])

        res = 0

        flag=None #prev sign
        count = 0
        for item in diff:
            if item==0:
                continue
            if flag==None:
                if item>0:
                    flag=True
                else:
                    flag=False
            else:
                if item>0 and not flag:
                    flag = True
                    pass
                elif item<0 and flag:
                    flag = False
                    pass
                else:
                    res=max(res,count+1)
                    count-=1
                    if item>0:
                        flag=True
                    else:
                        flag=False

            count+=1
        res=max(res,count+1)
            
        return res