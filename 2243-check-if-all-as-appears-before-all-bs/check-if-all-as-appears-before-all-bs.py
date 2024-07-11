class Solution:
    def checkString(self, s: str) -> bool:
        flag=False
        for i in s:
            if i=="b":
                flag=True
            elif flag:
                return False
        return True

            