class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        res = []
        seen = set()
        for item in names:
            if item not in seen:
                res.append(item)
                seen.add(item)
            else:
                num = 1
                new_item = item + f"({num})"
                while new_item in seen:
                    num += 1
                    new_item = item + f"({num})"
                res.append(new_item)
                seen.add(new_item)
        return res