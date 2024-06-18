class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res=[]
        potions.sort()

        def binSearch(arr,val):
            l=0
            r=len(arr)-1
            res=-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]*val<success:
                    res=mid
                    l=mid+1
                else:
                    r=mid-1
            print(mid,res,val)
            return res

        n=len(potions)
        for spell in spells:
            if spell*potions[0]>=success:
                count=n
            else:
                idx=binSearch(potions,spell)
                if idx==-1:
                    count=0
                else:
                    count=n-1-idx
            res.append(count)

        return res