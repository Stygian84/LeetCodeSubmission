class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        possible = []
        n = len(nums)
        temp = []
        for i in range(n):
            if nums[i]==0:
                if temp:
                    possible.append(temp)
                temp=[]
            else:
                temp.append(nums[i])
        possible.append(temp)
        

        maximum_length=0
        for item in possible:
            #check how many negative
            negative=0
            for num in item:
                if num<0:
                    negative+=1
            if negative%2==0:
                maximum_length = max(len(item),maximum_length)
            else:
                length = len(item)
                if length>maximum_length:
                    for i in range(length):
                        if item[i]<0:
                            break
                    for j in range(length-1,-1,-1):
                        if item[j]<0:
                            break
                    maximum_length = max(maximum_length,max(length-i-1,j))
        return maximum_length
