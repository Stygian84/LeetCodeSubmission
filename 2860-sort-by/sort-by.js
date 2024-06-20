/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    let res=arr;
    res.sort((a,b)=>fn(a)-fn(b))
    return res
};