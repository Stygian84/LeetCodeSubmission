class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        
        max_heap = []
        if a!=0:
            heapq.heappush(max_heap,(-a,'a'))
        if b!=0:
            heapq.heappush(max_heap,(-b,'b'))
        if c!=0:
            heapq.heappush(max_heap,(-c,'c'))            
            
        res = []
        n = a+b+c
        count = 0
        
        while max_heap:
            freq,letter = heapq.heappop(max_heap)
            
            if res and letter==res[-1]:
                if max_heap:
                    next_freq,next_letter = heapq.heappop(max_heap)
                    res.append(next_letter)
                    if next_freq+1<0:
                        heapq.heappush(max_heap,(next_freq+1,next_letter))
                else:
                    break
            if  freq<=-2:
                res.append(letter)
                res.append(letter)
                new_freq=freq+2
            else:
                res.append(letter)
                new_freq=freq+1
            
            if new_freq<0:
                heapq.heappush(max_heap,(new_freq,letter))
                
            
        
        return "".join(res)
            
        '''res=""
        #check which one is the greatest
        while True:
            max_value=max(a,b,c)
            if max_value>=2: 
                if a==max_value:
                    if res and res[-1]=='a':
                        break
                    a-=2
                    res+="aa"
                    if b>c:
                        if b==0:
                            continue
                        res+='b'
                        b-=1
                    else:
                        if c==0:
                            continue
                        res+='c'
                        c-=1
                elif b==max_value:
                    if res and res[-1]=='b':
                        break
                    b-=2
                    res+="bb"
                    if a>c:
                        if a==0:
                            continue
                        res+='a'
                        a-=1
                    else:
                        if c==0:
                            continue
                        res+='c'
                        c-=1
                else:
                    if res and res[-1]=='c':
                        break
                    c-=2
                    res+="cc"
                    if b>a:
                        if b==0:
                            continue
                        res+='b'
                        b-=1
                    else:
                        if a==0:
                            continue
                        res+='a'
                        a-=1
            else:
                break
        if a!=0 and res[-1]!='a':


        return res
        '''
        '''res=""
        max_value=max(a,b,c)
        while a!=b!=c and a>0 and b>0 and c>0:
            if max_value>2:
                if a==max_value:
                    a-=2
                    res+="aa"
                    if b>c:
                        res+='b'
                        b-=1
                    else:
                        res+='c'
                        c-=1
                elif b==max_value:
                    b-=2
                    res+="bb"
                    if a>c:
                        res+='a'
                        a-=1
                    else:
                        res+='c'
                        c-=1
                else:
                    c-=2
                    res+="cc"
                    if b>a:
                        res+='b'
                        b-=1
                    else:
                        res+='a'
                        a-=1

        
        while a==b==c and a>0:
            res+='abc'
            a-=1
            b-=1
            c-=1
        return res'''