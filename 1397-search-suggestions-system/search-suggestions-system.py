class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res=[]
        text=""
        for letter in searchWord:
            text+=letter
            ls=[]
            for item in products:
                if item.startswith(text):
                    ls.append(item)
            ls.sort()
            ls[:]=ls[:3]
            res.append(ls)
        return res