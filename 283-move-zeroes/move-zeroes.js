/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    n = nums.length
    if (n==1){
        return nums
    }
    let j = 0
    for (let i=0;i<n;i++){
        if (nums[i]!=0){
            [nums[i],nums[j]]=[nums[j],nums[i]]
            j+=1
        }
    }
    return nums
};