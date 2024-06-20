/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let res=[]
    let temp_ls=[]
    for (i=0;i<arr.length;i++){
        temp_ls.push(arr[i])
        if (temp_ls.length===size){
            res.push(temp_ls)
            temp_ls=[]
        }
    }
    if (temp_ls.length>=1 && temp_ls.length<size){
        res.push(temp_ls)
    }
    return res
    
};
