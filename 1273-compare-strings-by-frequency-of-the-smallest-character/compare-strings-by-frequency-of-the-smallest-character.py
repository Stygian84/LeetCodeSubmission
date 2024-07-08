class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            ls=sorted(s)
            count=0
            for item in ls:
                if item!=ls[0]:
                    return count
                count+=1
            return count
        
        res=[]
        
        for query in queries:
            count=0
            query_freq=f(query)

            for word in words:
                if f(word)>query_freq:
                    count+=1
            res.append(count)
        return res