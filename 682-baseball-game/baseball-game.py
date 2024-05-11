class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result=0
        record=[]
        for item in operations:
            if item=="C":
                record.pop()
                continue
            elif item=="D":
                record.append(record[-1]*2)
                
            elif item=="+":
                record.append(record[-1]+record[-2])
            else:
                record.append(int(item))
        return sum(record)