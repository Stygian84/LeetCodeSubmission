/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let res = []
    let j = 0
    
    while (j<arr.length){
        let temp = []
        for (i=0; i<size;i++){
            temp.push(arr[j])
            j++
            if (j>=arr.length){
                break
            }
        }
        res.push(temp)
    }

    return res
    
    
};
