class Solution:
    def checkString(self, s: str) -> bool:
        result=None
        if s[0]=='b' and s[-1]=='a':
            return False
        for item in s:
            if item=="a" and result==None:
                result=True
            elif result and item=="b":
                result=False
            elif result==False and item=="a":
                return False
            

        return True

            