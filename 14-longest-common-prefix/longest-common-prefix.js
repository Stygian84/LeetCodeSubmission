/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let n = Infinity
    let res = []

    for (let i = 0; i<strs.length;i++){
        if (strs[i].length<n){
            n = strs[i].length
        }
    }

    for (let i = 0 ; i<n; i++){
        res.push(strs[0][i])
        for (let j = 0;j<strs.length;j++){
            if (strs[j][i] == res[res.length-1]){
                continue
            }
            else{
                res.pop()
                return res.join("")
            }
        }
    }


    return res.join("")
};