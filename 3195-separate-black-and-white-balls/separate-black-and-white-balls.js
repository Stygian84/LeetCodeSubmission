/**
 * @param {string} s
 * @return {number}
 */
var minimumSteps = function(s) {
    let n = s.length
    let count = 0
    let zero = 0
    for (let i = n-1;i>-1;i--){
        if (s[i]==="1"){ count += zero}
        else { zero++ }
    }
    return count
};