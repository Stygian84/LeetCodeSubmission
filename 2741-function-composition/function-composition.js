/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    let ls=functions
    return function(x) {
        ls.reverse()
        res=x
        for(i=0;i<ls.length;i++){
            res=ls[i](res)
        }
        return res
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */