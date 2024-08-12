class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = [ x for x in range(1,m+1)]
        
        '''
        1 2 3 4 5
        3 1 2 4 5
        1 3 2 4 5
        '''

        result = []
        for q in queries:
            
            for i in range(m):
                if res[i]==q:
                    result.append(i)
                    break

            res = [q] + res[:i] + res[i+1:]
        
        return result
