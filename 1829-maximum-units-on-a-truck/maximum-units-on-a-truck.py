class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        result=0
        for item in boxTypes:
            if item[0]<=truckSize:
                truckSize-=item[0]
                result+=(item[0]*item[1])
            else:
                result+=(item[1]*truckSize)
                break

        return result
        