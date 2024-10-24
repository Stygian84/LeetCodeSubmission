class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        x,y,z = target
        first = False
        second = False
        third = False

        for a,b,c in triplets:
            if a>x or b>y or c>z:
                continue
            if a==x:
                first = True
            if b==y:
                second = True
            if c==z:
                third = True
                
        return first and second and third
        