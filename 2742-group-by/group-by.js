/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let groups={}

    this.forEach(item=>{
        let key=fn(item)
        if (groups[key]){
            groups[key].push(item)
        }else{
            groups[key]=[item]
        }
    })
    return groups
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */