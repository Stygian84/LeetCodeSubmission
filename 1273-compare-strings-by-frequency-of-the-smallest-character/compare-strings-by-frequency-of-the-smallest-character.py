class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            min_char = min(s)
            count = s.count(min_char)
            return count
        
        word_freqs = sorted(f(word) for word in words)
        res=[]
        
        for query in queries:
            query_freq=f(query)
            count = len(word_freqs) - bisect.bisect_right(word_freqs, query_freq)
            res.append(count)
        return res