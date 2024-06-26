class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        dc=defaultdict(int)
        for letter in t:
            dc[letter]+=1
        
        n=len(s)
        m=len(t)
        l,r=0,0

        formed=0
        window_count=defaultdict(int)
        min_length=math.inf
        min_window=""
        

        while r<n:
            letter = s[r]
            window_count[letter] += 1

            if letter in dc and window_count[letter] == dc[letter]:
                formed+=1
            
            while formed == len(dc) and l<=r:
                current_length = r-l+1

                if current_length < min_length :
                    min_length = current_length
                    min_window = s[l:r+1]
                
                window_count[s[l]] -= 1
                if s[l] in dc and window_count[s[l]]<dc[s[l]]:
                    formed-=1
                l+=1
            r+=1
            
        
        return min_window
        '''dc=defaultdict(int)
        for letter in t:
            dc[letter]+=1

        n=len(s)
        min_length=math.inf
        i=0
        res=""

        
        for j in range(n):
            if s[j] in dc:
                dc[s[j]]-=1

            while all(value<=0 for value in dc.values()):
                if j-i+1<min_length:
                    min_length=j-i+1
                    res=s[i:j+1]
                if s[i] in dc:
                    dc[s[i]]+=1
                i+=1
            

        return res'''
        