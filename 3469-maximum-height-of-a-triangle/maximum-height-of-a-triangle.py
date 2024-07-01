class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        def maxHeight(red,blue):
            count=0
            i=1

            while red>=0 and blue>=0:
                if i%2==0: # blue
                    blue-=i
                    if blue<0:  break
                else: # red
                    red-=i
                    if red<0: break
                count+=1
                i+=1

            return count

        return max(maxHeight(blue,red),maxHeight(red,blue))