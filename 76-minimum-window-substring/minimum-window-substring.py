class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        target_counts = defaultdict(int)
        for char in t:
            target_counts[char] += 1
        
        required_chars = len(target_counts)
        left, right = 0, 0
        formed = 0
        window_counts = defaultdict(int)
        min_len = float('inf')
        min_window = ""
        
        while right < len(s):
            char = s[right]
            window_counts[char] += 1
            
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
            
            while formed == required_chars and left <= right:
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    min_window = s[left:right+1]
                
                window_counts[s[left]] -= 1
                if s[left] in target_counts and window_counts[s[left]] < target_counts[s[left]]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
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
        