/**
 * @param {string} s
 * @param {string} target
 * @return {number}
 */
var rearrangeCharacters = function(s, target) {
    let freq_s = {}
    let freq_target = {}

    for (letter of target){
        freq_target[letter] = (freq_target[letter] || 0) + 1
        
    }
    for (letter of s){
        if (letter in freq_target){
            freq_s[letter] = (freq_s[letter] || 0)+1
        }
    }
    if (Object.keys(freq_s).length!==Object.keys(freq_target).length){
        return 0
    }
    let minimum = Infinity
    for (key of Object.keys(freq_s)){
        if (freq_s[key]<freq_target[key]){
            return 0
        }
        minimum = Math.min(minimum,Math.floor(freq_s[key]/freq_target[key]))
    }
    return minimum
};