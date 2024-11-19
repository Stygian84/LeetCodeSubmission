class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        window = deque([])

        n = len(word)
        res = 0
        check = "aaeiou"
        j = 1

        for i in range(n):
            if word[i] == check[j]:
                window.append(word[i])
                j+=1
                if j >= len(check):
                    j = len(check)-1
            elif word[i] == check[j-1] and window and window[-1]==check[j-1]:
                window.append(word[i])
            else:
                if window and window[-1]==check[-1]:
                    res = max(res,len(window))
                window = deque([])
                j = 1
                if word[i] == 'a':            
                    window.append('a')
                    j+=1

        if window and window[-1]==check[-1]:
            res = max(res,len(window))

        return res
