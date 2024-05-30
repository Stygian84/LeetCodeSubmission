class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        res=[0]*len(boxes)
        for idx in range(len(res)):
            count=0
            for i in range(len(boxes)):
                if boxes[i]=="1":
                    count+=abs(idx-i)

            res[idx]=count
        return res