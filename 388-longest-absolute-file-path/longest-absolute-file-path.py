class Solution:
    def lengthLongestPath(self, input: str) -> int:
        count=0  
        ls=input.split("\n")
        max_length=0
        dc={}
        for item in ls:
            count=item.count("\t")
            depth= count
            if "." in item:
                max_length=max(max_length,dc.get(depth,0)+len(item[count:]))
            else:
                dc[depth+1]=dc.get(depth,0)+len(item[count:])+1
        return max_length