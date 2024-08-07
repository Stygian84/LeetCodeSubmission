class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        n = len(tiles)
        count = 0
        seen = set()
        freq = Counter(tiles)
        def backtrack(path,freq):
            nonlocal count
            
            if path:
                count+=1
            if len(path)==n:
                return

            for i in range(n):
                path.append(tiles[i])
                freq[tiles[i]]-=1
                if tuple("".join(path)) not in seen and freq[tiles[i]]>=0:
                    seen.add(tuple("".join(path)))
                    backtrack(path,freq)
                freq[tiles[i]]+=1
                path.pop()

        backtrack([],freq)
        return count
        '''if len(tiles)==1:
            return 1

        def backtrack( path):
            result.append(path[:])
            
            for i in range(len(tiles)):
                path.append(tiles[i])
                backtrack(path)
                path.pop()
            return
        
        result = []
        backtrack([])
        print(result)
        return len(result)
        '''