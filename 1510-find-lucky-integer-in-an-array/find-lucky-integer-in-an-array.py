class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        for item in arr:
            if arr.count(item)==item:
                return item
        return -1
        