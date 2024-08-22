/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    minimum=Infinity
    res=-Infinity

    for (let i = 0;i<prices.length;i++){
        if (prices[i]<minimum){
            minimum=prices[i]
        }
        else if (prices[i]-minimum>res){
            res = prices[i]-minimum
        }
    }
    if ((res<0) || (res==-Infinity)){
        return 0
    }
    return res
};