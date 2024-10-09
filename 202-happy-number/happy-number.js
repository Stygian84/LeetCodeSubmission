/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let seen = new Set()
    seen.add(n)
    n = String(n)
    
    while (true){
        let total = 0

        for (digit of n){
            total += Number(digit)**2
        }
        if (total==1){
            return true
        }
        if (seen.has(total)){
            return false
        }
        seen.add(total)
        
        n = String(total)
    }
};