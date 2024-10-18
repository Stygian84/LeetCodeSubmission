class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # times 2 or minus 1
        #if from target, if divisible by 2 divide by 2 then minus 1
        count = 0
        if startValue>target:
            return startValue-target

        while target!=startValue:
            while target%2==0 and target>startValue:
                count += 1
                target //= 2

            if target==startValue:
                break
            target += 1
            count+=1

        return count
                