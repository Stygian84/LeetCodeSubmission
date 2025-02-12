function maximumSum(nums: number[]): number {
    nums.sort((a, b) => a - b)
    let storage = new Map<number, number[]>()

    for (let i = 0; i < nums.length; i++) {
        let str_num = nums[i].toString();
        let total = 0
        for (let digit of str_num) {
            total += Number(digit)
        }
        if (!storage.has(total)) {
            storage.set(total, [])
        }
        storage.get(total).push(nums[i])
    }

    let res = -1
    storage.forEach((value,key) => {
        let n = value.length
        if (n >= 2) {
            res = Math.max(res, value[n - 1] + value[n - 2])
        }
    })
    return res
};