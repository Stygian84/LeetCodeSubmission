/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let res = []
    let dict = {}

    for (let i=0; i<nums.length; i++){
        diff = target-nums[i]
        if (diff in dict){
            res.push(dict[diff])
            res.push(i)
            break
        }
        dict[nums[i]]=i
    }
    return res
};