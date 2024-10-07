/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    
    n = s.length
    let res = s[0]
    for (let i = 0 ; i<n;i++){
        let j = 1
        // consider odd
        while (i-j>=0 && i+j<n){
            if (s[i+j]==s[i-j]){
                if (2*j+1 > res.length){
                    res = s.slice(i-j,i+j+1)
                }
                j+=1
            }
            else{
                break
            }
        } 

        //consider even
        if (i+1<n && s[i]==s[i+1]){ 
            if (2>res.length){
                res = s[i]+s[i+1]
            }
            j=1
            
            while (i-j>=0 && i+j+1<n){
                if (s[i+j+1]==s[i-j]){
                    if (2*j+2 > res.length){
                        res = s.slice(i-j,i+1+j+1)
                    }
                    j+=1
                }
                else{
                    break
                }
            } 
        }
    }
    return res
};