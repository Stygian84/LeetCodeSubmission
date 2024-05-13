class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter=0
        for item in arr:
            if arr.count(item) ==1:
                counter+=1
                if counter==k:
                    return item
        return ""