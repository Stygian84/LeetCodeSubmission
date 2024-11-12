class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort()
        temp = [items[0]]
        maximum = items[0][1]
        for i in range(1,len(items)):
            if items[i][1]>maximum: 
                maximum = items[i][1]
                temp.append(items[i])

        n = len(temp)

        res = []

        for q in queries:
            l=0
            r=n-1
            result = 0

            while l<=r:
                mid = (l+r)//2
                price,beauty = temp[mid]
                if price<=q:
                    result = beauty
                    l=mid+1
                elif price>q:
                    r=mid-1
            # 1 2 3 3 5
            res.append(result)
        return res
