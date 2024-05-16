class Solution:
    def finalString(self, s: str) -> str:
        result=""
        for item in s:
            if item=="i":
                result=result[::-1]
                continue
            result+=item
        return result        