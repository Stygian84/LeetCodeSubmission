class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q=deque(senate)
        dc={"R":"Radiant","D":"Dire"}
        while len(q)>1:
            senate= q.popleft()
            temp_q=deque()
            while q and q[0]==senate:
                temp_q.append(q.popleft())
            if q:
                q.popleft()
            q.extendleft(temp_q)
            q.append(senate)
            if len(set(q))==1:
                break
        return dc[senate]