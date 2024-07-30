class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        prefix_sum = [[0]*26 for _ in range(n+1)]

        for i in range(n):
            char_idx = ord(s[i]) - ord('a')
            for j in range(26):
                prefix_sum[i+1][j] = prefix_sum[i][j]
            prefix_sum[i+1][char_idx]+=1
        
        total = 0
        
        for i in range(n):
            for j in range(i+1,n+1):
                substring = s[i:j]
                maximum = -math.inf
                minimum = math.inf

                for k in range(26):
                    count = prefix_sum[j][k] - prefix_sum[i][k]
                    if count > 0: 
                        maximum = max(maximum, count)
                        minimum = min(minimum, count)

                if maximum != -math.inf and minimum != math.inf:
                    total += maximum - minimum
        return total
        '''ls = deque()

        dc = defaultdict(int)

        total = 0
        for letter in s:
            ls.append(letter)
            dc[letter]+=1
            if len(dc)==1:
                continue
            total += max(dc.values()) - min(dc.values())
            print(dc, total , ls)
        
        for i in range(len(ls)):
            letter = ls.popleft()
            dc[letter]-=1
            if dc[letter]==0:
                del dc[letter]
            if len(dc)==1:
                break
            total+= max(dc.values()) - min(dc.values())
            print(dc, total, ls)

        return total'''
            