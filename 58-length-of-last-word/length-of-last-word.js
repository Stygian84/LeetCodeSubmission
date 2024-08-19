/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let ls = s.trim().split(" ")
    let n = ls.length
    
    return ls[n-1].length
};