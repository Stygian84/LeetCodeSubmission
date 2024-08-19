/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let i = 1
    let not_val_idx = 1
    let count = 0
    let n = nums.length
    if (n==1){
        return n
    }

    while (i<n){
        if (nums[i]!=nums[i-1]){
            nums[not_val_idx]=nums[i]
            not_val_idx++
        }
        else{
            count++
        }
        i++
    }
    return n-count
};