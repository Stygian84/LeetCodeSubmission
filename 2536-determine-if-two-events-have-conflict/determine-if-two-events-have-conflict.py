class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        if event2[0]<=event1[1] and event2[1]>=event1[0]:
            return True
        return False