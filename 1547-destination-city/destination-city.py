class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dc={}
        location={}
        for item in paths:
            dc[item[0]]=dc.get(item[0],0)+1
            dc[item[1]]=dc.get(item[1],0)+1
            location[item[0]]=0
            location[item[1]]=1
        print(dc,location)
        for key,values in dc.items():
            if values==1:
                if location[key]==1:
                    return key
        