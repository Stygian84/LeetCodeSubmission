class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # replace brackets in s with knowledge[name]
        dictionary = {}
        for a,b in knowledge:
            dictionary[a]=b
        
        res = []
        check = False

        temp = ""
        for item in s:
            if item=="(":
                check = True
                res.append(temp)
                temp = ""
                continue

            elif item==")":
                check = False
                if temp in dictionary:
                    res.append(dictionary[temp])
                else:
                    res.append("?")
                temp = ""
                continue

            temp+=item

        if temp:
            res.append(temp)
        
        return "".join(res)