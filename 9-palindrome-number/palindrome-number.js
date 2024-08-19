/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x<0){
        return false
    }
    let a = x.toString()
    
    let i=0
    let j=a.length-1

    while (i<j){
        if (a[i]!==a[j]){
            return false
        }
        i++
        j--
    }
    return true
    /*
    a=x.toString()
    return a===a.split("").reverse().join("")
    */
};