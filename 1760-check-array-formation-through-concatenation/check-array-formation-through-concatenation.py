class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dc={}
        for piece in pieces:
            dc[piece[0]]=piece
        
        i=0
        while i<len(arr):
            element=arr[i]
            
            if element in dc:
                n = len(dc[element])
                
                if arr[i:i+n]== dc[element]:
                    i+=n
                    continue
                else:
                    return False
            else:
                return False
        return True
        