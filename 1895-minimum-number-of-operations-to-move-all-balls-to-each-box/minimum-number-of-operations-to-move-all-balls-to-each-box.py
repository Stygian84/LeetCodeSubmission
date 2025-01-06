class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        location = defaultdict(int)

        for i in range(len(boxes)):
            if boxes[i]=="1":
                location[i]+=1
        
        res = []
        for i in range(len(boxes)):
            total = 0
            for j in location.keys():
                total += abs(j-i)
            res.append(total)
        
        return res