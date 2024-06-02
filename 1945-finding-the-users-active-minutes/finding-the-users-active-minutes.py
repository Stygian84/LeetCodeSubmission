class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res=[0]*k
        dc={}
        for item in logs:
            dc[item[0]]=dc.get(item[0],set())
            dc[item[0]].add(item[1])
        for values in dc.values():
            res[len(values)-1]+=1
        return res
        