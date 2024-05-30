class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        '''
        res=[0]*len(boxes)
        for idx in range(len(res)):
            count=0
            for i in range(len(boxes)):
                if boxes[i]=="1":
                    count+=abs(idx-i)

            res[idx]=count
        return res
        '''
        n = len(boxes)
        res = [0] * n
        
        count, total = 0, 0
        for i in range(n):
            total += count
            res[i] = total
            if boxes[i] == '1':
                count += 1
        
        count, total = 0, 0
        for i in range(n-1, -1, -1):
            total += count
            res[i] += total
            if boxes[i] == '1':
                count += 1
                
        return res