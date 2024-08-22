/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let n = digits.length
    let i = n-1
    let val = 1
    while (true){
        let temp = digits[i]+val
        digits[i] = temp%10
        if (temp>=10){
            val = Math.floor(temp/10)
            i--
        }
        else{
            break
        }
    }
    if (i<0){
        digits.unshift(val)
    }
    return digits
};