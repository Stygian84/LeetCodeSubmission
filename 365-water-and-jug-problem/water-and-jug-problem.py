class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        z = target
        if(x + y < z): return False
        if( x == z or y == z or x + y == z ): return True
        
        return z%math.gcd(x, y) == 0
        '''if target==x+y:
            return True
        diff = abs(y-x)
        if target==diff:
            return True
        if target==y-(x-diff) or target==x-(y-diff):
            return True
        if target==y-(x-diff)+x or target==x-(y-diff)+y:
            return True
        if target%diff==0:
            return True
        return False'''