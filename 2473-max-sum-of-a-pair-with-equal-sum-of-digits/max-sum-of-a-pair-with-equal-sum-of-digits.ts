function maximumSum(nums: number[]): number {
    let storage = new Map<number, number>()
    let res = -1

    for (let i = 0; i < nums.length; i++) {
        let total = 0
        let temp = nums[i]
        while (temp>0){
            total += temp%10
            temp = Math.floor(temp/10)
        }
        
        if (!storage.has(total)) {
            storage.set(total, nums[i])
        }
        else {
            let compared = storage.get(total)
            res = Math.max(res, compared + nums[i])
            if (nums[i] > compared) {
                storage.set(total, nums[i])
            }
        }

    }

    return res
};