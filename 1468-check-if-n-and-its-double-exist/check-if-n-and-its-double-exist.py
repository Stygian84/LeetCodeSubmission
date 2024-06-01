class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for item in arr:
            if item*2 in arr:
                if item==0 and arr.count(item)==1:
                    continue
                return True
        return False
        