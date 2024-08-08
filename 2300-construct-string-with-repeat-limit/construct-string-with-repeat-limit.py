class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        dc = Counter(s)
        heap = []

        for letter in dc:
            heapq.heappush( heap, (-ord(letter),dc[letter]) )
        
        n= len(s)
        res = []
        while heap:
            letter,freq = heapq.heappop(heap)
            letter = chr(-letter)

            if freq <= repeatLimit:
                res.append( letter*(freq) )
                continue
            
            else:
                res.append( letter*(repeatLimit) )
                if heap:
                    second_letter,second_freq = heapq.heappop(heap)
                    second_letter = chr(-second_letter)

                    res.append( second_letter )
                    if second_freq-1 > 0:
                        heapq.heappush( heap, (-ord(second_letter),second_freq-1) )
                    if freq-repeatLimit > 0:
                        heapq.heappush( heap, (-ord(letter),freq-repeatLimit) )
                else:
                    return "".join(res)

        return "".join(res)
        
        '''
        heap = []
        dc = Counter(s)
        for letter in dc:
            heapq.heappush(heap,(letter,-dc[letter]))

        n = len(s)
        res = []
        while heap:
            letter,count = heapq.heappop(heap)
            count = -count
            if count<=repeatLimit:
                res.append(letter*count)
            else:
                new,new_count = heapq.heappop(heap)
                new_count=-new_count
                while count>repeatLimit:
                    res.append(letter*repeatLimit)
                    count-=repeatLimit
                    res.append(new)
                    new_count-=1
                    if new_count==0:
                        break
                res.append(letter*count)
                
                if new_count != 0 :
                    heapq.heappush(heap, (new,-new_count) )
                if count>0:
                    heapq.heappush(heap, (letter,-count) )            
        return "".join(res)'''