/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    a=x.toString()
    return a===a.split("").reverse().join("")
};