class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key= lambda x:(-x[0],x[1]))
        n = len(properties)
        

        max_defense = 0
        count=0

        for a,d in properties:
            if d<max_defense:
                count+=1
            else:
                max_defense=d
        return count