class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        
        ls = []
        for v,l in zip(values,labels):
            ls.append((v,l))
        ls.sort(reverse=True)

        count = 0
        total = 0
        i = 0
        labels = defaultdict(int)

        print(ls)
        while i<len(ls) and count<numWanted:
            

            while i<len(ls) and labels[ls[i][1]]>=useLimit:
                label = ls[i][1]
                i+=1

            if i<len(ls):
                count+=1
                labels[ls[i][1]]+=1
                total+=ls[i][0]
                i+=1
                

        return total
            
        
        '''
        dc=defaultdict(list)
        for v,l in zip(values,labels):
            dc[v].append(l)
        
        values.sort(reverse=True)
        res=0
        used_labels=set()
        i=0
        count=0
        while i <len(values):
            if count==numWanted-1:
                break
            res+=values[i]
            count+=1
            i+=1
            used_labels.add(dc[values[i]][0])
            if len(used_labels)==useLimit:
                if count<numWanted-1:
                    i+=1
                    continue
                break

        return res
        '''