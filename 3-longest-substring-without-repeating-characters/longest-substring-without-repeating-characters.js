/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let seen = new Set()
    let left = 0
    let right = 0
    let n = s.length
    let res = 0
    while (right<n){
        while (seen.has(s[right])){
            seen.delete(s[left])
            left+=1
        }
        seen.add(s[right])
        if (right-left+1>res){
            res = right-left+1
        }
        right+=1
    }
    return res
};