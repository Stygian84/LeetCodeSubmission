/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = []
    let n = s.length

    let matching = {")":"(","]":"[","}":"{"}
    for (let i=0;i<n;i++){

        if (s[i] in matching){
            if ((stack) && (stack.pop()==matching[s[i]])){
                continue
            }
            else{
                return false
            }
        }
        else{
            stack.push(s[i])
        }

    }

    if (stack.length==0){
        return true
    }
    return false
};