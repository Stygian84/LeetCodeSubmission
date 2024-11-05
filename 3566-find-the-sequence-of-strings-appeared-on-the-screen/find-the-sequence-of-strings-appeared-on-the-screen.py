class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = ["a"]

        while res[-1] != target:

            current = res[-1]
            length = len(current)
            
            if current[length-1] != target[length-1]:
                res.append(current[:-1] + chr(ord(current[-1])+1))
            
            elif len(current)<len(target):
                res.append(current+'a')
        
        return res