class Solution:
    def toLowerCase(self, s: str) -> str:
        result=""
        for item in s:
            if 65<=ord(item)<91:
                result+=chr(ord(item)+32)
            else:
                result+=item
        return result

        