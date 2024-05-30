class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ls=[-1]
        for item in arr[::-1]:
            if item in ls:
                continue
            else:
                if arr.count(item)==item:
                    ls.append(item)
        return max(ls)
        