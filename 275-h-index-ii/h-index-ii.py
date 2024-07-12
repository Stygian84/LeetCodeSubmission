class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        i = 0
        j = n-1

        res = 0
        while i<=j:
            mid = (i+j)//2
            item = citations[mid]
            print(mid,item)
            if item >= n-mid:
                j = mid-1
            else:
                i = mid+1
        return n-i
