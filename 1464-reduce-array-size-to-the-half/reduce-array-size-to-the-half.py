class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dc={}
        for item in arr:
            dc[item]=dc.get(item,0)+1
        n=len(arr)
        freq=[]
        for value in dc.values():
            freq.append(value)
        freq.sort()
        count=0

        while True and freq:
            size=freq.pop()
            count+=1
            n-=size
            if n<=(len(arr)/2):
                
                break
        return count
        