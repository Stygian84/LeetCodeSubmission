class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)

        dc=defaultdict(list)
        for i in range(n):
            sorted_str="".join(sorted(list(strs[i])))
            dc[sorted_str].append(i)

        res=[]
        for value in dc.values():
            temp=[]
            for v in value:
                temp.append(strs[v])
            res.append(temp)
        

        return res