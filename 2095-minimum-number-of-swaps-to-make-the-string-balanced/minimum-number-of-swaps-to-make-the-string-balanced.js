/**
 * @param {string} s
 * @return {number}
 */
var minSwaps = function(s) {
    let balance = 0
    let swap = 0

    for (let i = 0 ; i<s.length;i++){
        if (s[i]=="["){
            balance += 1
        }
        else if (s[i]=="]"){
            balance -= 1
        }
        if (balance<0){
            //console.log(s[i],balance,swap)
            swap += 1
            balance+=2
        }
    }
    return swap
    
};