class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen=[]
        ans=[]
        k=0
        for item in nums:
            if item >0:
                k=0
                seen.insert(0,item)
            if item==-1:
                k+=1
                
                print(seen,k)
                if k>0:
                    if k<=len(seen):
                        ans.append(seen[k-1])
                    else:
                        ans.append(-1)
        return ans

        