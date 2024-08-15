class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
        def isBulky():
            volume = length*width*height
            return volume>=10**9 or (length>=10**4) or (height>=10**4) or (width>=10**4)
        
        def isHeavy():
            return mass>=100
        
        if isHeavy() and not isBulky():
            return "Heavy"
        if not isHeavy() and isBulky():
            return "Bulky"
        if isHeavy() and isBulky():
            return "Both"
        else:
            return "Neither"