function lengthOfLongestSubstring(s: string): number {

    let res = 0;
    let left = 0;
    let index = new Map<string,number>();

    for (let right=0;right<s.length;right++){
        if (index.has(s[right])){
            left = Math.max(left,index.get(s[right])+1)
        }
        index.set(s[right],right)
        res = Math.max(res,right-left+1)
    }
    return res
};