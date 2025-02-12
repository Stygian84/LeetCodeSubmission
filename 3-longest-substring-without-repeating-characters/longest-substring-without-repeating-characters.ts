function lengthOfLongestSubstring(s: string): number {

    let res = 0;
    let temp = [];

    for (let i = 0; i < s.length; i++) {
        while (temp.includes(s[i])) {
            temp.shift()
        }
        temp.push(s[i])
        if (temp.length > res) {
            res = temp.length
        }
    }
    return res
};