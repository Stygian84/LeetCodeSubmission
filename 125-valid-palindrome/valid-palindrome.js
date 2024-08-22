/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
    function isAlNum(char) {
        return /^[a-zA-Z0-9]$/.test(char);
    }

    let temp = []
    for (let i = 0; i < s.length; i++) {
        if ((s[i] != " ")&(isAlNum(s[i]))) {
            temp.push(s[i].toLowerCase())
        }
    }
    return temp.join("") === temp.slice().reverse().join("")
};