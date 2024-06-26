class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dc=defaultdict(int)
        for letter in t:
            dc[letter]+=1

        n=len(s)
        min_length=math.inf
        i=0
        res=""

        dc2=copy.copy(dc)
        for j in range(n):
            if s[j] in dc2:
                dc2[s[j]]-=1

            while all(value<=0 for value in dc2.values()):
                if j-i+1<min_length:
                    min_length=j-i+1
                    res=s[i:j+1]
                if s[i] in dc2:
                    dc2[s[i]]+=1
                i+=1
            

        return res

        '''l=0
        r=0
        dc={}
        for item in t:
            dc[item]=dc.get(item,0)+1
        temp_str=deque([])
        while r<len(t)-1:
            letter=s[r]
            temp_str.append(s[r])
            if letter in dc:
                dc[letter]-=1
            r+=1
            while all(value<=0 for value in dc.values()):
                left_letter=s[l]
                if left_letter in dc:
                    if dc[left_letter]+1>0:
                        break
                    else:
                        dc[left_letter]+=1
                temp_str.popleft()
                l+=1
        return "".join(temp_str)'''