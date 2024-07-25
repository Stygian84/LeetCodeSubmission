class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        diff=[]
        n = len(nums)
        for i in range(1,n):
            diff.append(nums[i]-nums[i-1])

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
                elif item<0 and flag:
                    flag = False
                else:
                    count-=1
                    if item>0:
                        flag=True
                    else:
                        flag=False

            count+=1
            
        return count+1