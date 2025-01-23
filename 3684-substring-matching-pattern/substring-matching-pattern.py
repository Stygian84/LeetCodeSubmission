class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        ls = p.split("*")
        left = ls[0]
        right = ls[1]
        
        left_idx = s.find(left)
        
        right_idx = s[left_idx+len(left):].find(right) 

        if left and left_idx == -1:
            return False
        if right and right_idx == -1:
            return False
        return True

        
        