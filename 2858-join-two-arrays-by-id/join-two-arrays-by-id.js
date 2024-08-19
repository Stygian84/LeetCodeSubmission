/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let dict = {}

    for (i=0;i<arr2.length;i++){
        dict[arr2[i].id]=arr2[i]
    }

    for (i=0;i<arr1.length;i++){
        
        if (arr1[i].id in dict){
            for (let key in arr1[i]){
                if (!(key in dict[arr1[i].id])){
                    dict[arr1[i].id][key] = arr1[i][key]
                }
            }
        }
        else{
            dict[arr1[i].id]=arr1[i]
        }        
    }

    res = []
    for (key in dict){
        res.push(dict[key])
    }

    res.sort((a,b)=>a.id-b.id)

    return res

};