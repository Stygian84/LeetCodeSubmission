function maximumSum(nums: number[]): number {
    let storage = new Map<number, number>()
    let res = -1

    for (let i = 0; i < nums.length; i++) {
        let str_num = nums[i].toString();
        let total = 0
        for (let digit of str_num) {
            total += Number(digit)
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