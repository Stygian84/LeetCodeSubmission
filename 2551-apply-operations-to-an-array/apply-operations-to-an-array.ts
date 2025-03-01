function applyOperations(nums: number[]): number[] {
    let res : number[] = [];
    for(let i=0;i<nums.length;i++){
        res.push(0)
    }
    let j=0;
    let n = nums.length
    for (let i=0;i<n-1;i++){
        if (nums[i]!=0){
            if (nums[i]==nums[i+1]){
                res[j]=nums[i]*2
                nums[i+1]=0
            }
            else{
                res[j]=nums[i]
            }
            j+=1
        }
        console.log(i,res)
    }
    if (nums[n-1]!=0){
        res[j]=nums[n-1]
    }
    
    return res
};