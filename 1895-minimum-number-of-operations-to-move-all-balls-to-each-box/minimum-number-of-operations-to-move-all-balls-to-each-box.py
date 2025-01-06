class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        res = [0]*len(boxes)

        total,count = 0,0
        for i in range(len(boxes)):
            box = boxes[i]
            res[i] += total
            if box=="1":
                count+=1
            total+=count
        
        total,count = 0,0
        for i in range(len(boxes)-1,-1,-1):
            box = boxes[i]
            res[i] += total
            if box=="1":
                count+=1
            total+=count
        return res