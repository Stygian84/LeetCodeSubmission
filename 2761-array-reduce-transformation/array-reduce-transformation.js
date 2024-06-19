/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    res=init
    for (i=0;i<nums.length;i++){
        res=fn(res,nums[i])
    }
    return res
};