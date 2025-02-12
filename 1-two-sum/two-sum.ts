function twoSum(nums: number[], target: number): number[] {
    const indexDict = new Map<number, number>()
    let res = []

    for (let i = 0; i<nums.length;i++){
        let diff = target-nums[i]
        if (indexDict.has(diff)){
            res = [indexDict.get(diff),i]
        }
        else{
            indexDict.set(nums[i],i)
        }
        //console.log(indexDict)
    }
    return res
};