class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        if len(bank)==1:
            return 0

        total=0
        
        i=0
        prev_count=None
        while i<len(bank):
            current_count=bank[i].count("1")
            if current_count!=0:
                if prev_count is not None:
                    total += current_count * prev_count
                prev_count = current_count
            i+=1

        return total