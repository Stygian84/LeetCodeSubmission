/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    let i = 0
    let j = nums.length-1

    let ls = []
    nums.forEach((item,index)=>{
        ls.push([item,index])
    })
    ls.sort( (a,b)=> a[0]-b[0] )

    while (i<j){
        total = ls[i][0]+ls[j][0]
        if (total == target){
            return [ls[i][1],ls[j][1]]
        }
        else if (total<target){
            i++
        }
        else{
            j--
        }
    }
    console.log(ls)
};