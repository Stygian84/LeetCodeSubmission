/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let n = nums.length

    let mid = Math.floor(n/2)
    nums.sort((a,b)=>a-b)
    return nums[mid]
};