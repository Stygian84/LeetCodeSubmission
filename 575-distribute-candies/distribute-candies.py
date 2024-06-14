class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        dc={}
        n=len(candyType)/2
        for item in candyType:
            dc[item]=dc.get(item,0)+1
        count=0
        for value in dc.values():
            n-=1
            count+=1
            if n==0:
                return count
        return count