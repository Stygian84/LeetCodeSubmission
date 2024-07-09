class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num_str=str(n)
        n_digits=len(num_str)
        temp_ls=[]
        def find_power_range(n_digits):
            power = 0
            while True:
                current_power = 2 ** power
                num_digits = len(str(current_power))
                
                if num_digits == n_digits:
                    temp_ls.append(current_power)
                if num_digits > n_digits:
                    return
                
                power += 1
        find_power_range(n_digits)
        
        if n<=10:
            return n in temp_ls
        ls = list(num_str)
        ls.sort()
        sorted_num="".join(ls)
        
        for i in range(len(temp_ls)):
            temp_ls[i]="".join(sorted(list(str(temp_ls[i]))))
        return sorted_num in temp_ls