class Solution:
    def checkRecord(self, s: str) -> bool:
        absent=0
        late=0
        for item in s:
            if item == "A":
                absent+=1
                if absent==2:
                    return False
            elif item == "L":
                late+=1
                if late==3:
                    return False
                continue
            late=0
        return True
