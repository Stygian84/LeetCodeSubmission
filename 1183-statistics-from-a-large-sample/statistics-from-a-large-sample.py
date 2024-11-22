class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        

        freq = defaultdict(int)
        minimum = math.inf
        maximum = None

        total = 0
        n = 0
        mode_freq = 0
        mode = 0
        for i in range(256):
            freq[i] += count[i]
            if minimum == math.inf and count[i]>0:
                minimum = i
            if count[i]>0:
                maximum = i
            
            n += count[i]
            total += i*count[i]
            if count[i]>mode_freq:
                mode_freq = count[i]
                mode = i

        mean = total/n
        
        if n%2==0:
            find = n//2
            find2 = n//2+1
            median = 0
            
            for k,v in freq.items():
                find-=v
                find2-=v
                if find<=0:
                    median += k
                    find = math.inf

                if find2<=0:
                    median += k
                    find2 = math.inf

                if find == find2 == math.inf:
                    break
                
            median /= 2

        else:
            find = n//2+1

            for k,v in freq.items():
                find -= v
                if find<=0:
                    median = k
                    break
        return [minimum,maximum,mean,median,mode]