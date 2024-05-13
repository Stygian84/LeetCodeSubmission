class Solution:
    def partitionString(self, s: str) -> int:
        ls=[]
        temp_str=""
        for item in s:
            print(temp_str,item)
            if item not in temp_str:
                temp_str+=item
            else:
                ls.append(temp_str)
                temp_str=item 
        print(ls)
        return len(ls)+1