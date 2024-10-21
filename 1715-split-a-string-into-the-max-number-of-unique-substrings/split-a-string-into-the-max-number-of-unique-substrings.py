class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        n=len(s)
        res = 0
        def dfs(start,path,seen):
            nonlocal res
            if start == n:
                res = max(res,len(path[:])) 
                return

            for i in range(start,n):
                if s[start:i+1] not in seen:
                    path.append(s[start:i+1])
                    seen.add(s[start:i+1])

                    dfs(i+1,path,seen)

                    seen.remove(s[start:i+1])
                    path.pop()
        
        dfs(0,[],set())
        return res

        '''seen = set()

        i = 0
        j = 0
        n = len(s)
        while j<n:
            if s[j] not in seen:
                seen.add(s[j])
                i=j
            else:
                if s[i:j] not in seen:
                    seen.add(s[i:j])
                    i=j
            j+=1
        #if i!=n-1:
        #    seen.add(s[i:j])
        print(seen)
        return len(seen)'''