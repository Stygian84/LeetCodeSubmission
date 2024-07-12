class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a = sum(aliceSizes)
        b = sum(bobSizes)
        fair = abs(b - a)//2
        #print(fair)
        aliceSizes.sort()
        bobSizes.sort()

        if a<b:
            for item in aliceSizes:
                i=0
                j=len(bobSizes)
                
                while i<=j:
                    mid=(i+j)//2
                    item2=bobSizes[mid]
                    if item2-item==fair:
                        return [item,item2]
                    elif item2-item>fair:
                        j=mid-1
                    else:
                        i=mid+1
        else:
            for item in bobSizes:
                i=0
                j=len(aliceSizes)
                
                while i<=j:
                    mid=(i+j)//2
                    item2=aliceSizes[mid]
                    if item2-item==fair:
                        return [item2,item]
                    elif item2-item>fair:
                        j=mid-1
                    else:
                        i=mid+1
            