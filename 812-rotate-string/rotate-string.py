class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        for i in range(len(goal)):
            if goal[i:]+goal[:i]==s:
                return True
        return False