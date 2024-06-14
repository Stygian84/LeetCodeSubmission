class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        visited=[False]*n
        def dfs(room):
            visited[room]=True
            for key in rooms[room]:
                if not visited[key]:
                    dfs(key)        
        dfs(0)
        if all(value==True for value in visited):
            return True
        else:
            return False
