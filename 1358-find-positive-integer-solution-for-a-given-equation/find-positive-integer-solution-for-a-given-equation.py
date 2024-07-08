"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        x, y = 1, 101  

        while x <= 101 and y >= 1:
            value = customfunction.f(x, y)
            if value == z:
                res.append([x, y])
                x += 1  
                y -= 1  
            elif value < z:
                x += 1  
            else:
                y -= 1  
        
        return res