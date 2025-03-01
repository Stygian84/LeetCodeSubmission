function applyOperations(nums: number[]): number[] {
    
    let j=0;
    let n = nums.length
    for (let i=0;i<n-1;i++){
        if (nums[i]!=0){
            if (nums[i]==nums[i+1]){
                nums[j]=nums[i]*2
                nums[i+1]=0
            }
            else{
                nums[j]=nums[i]
            }
            j+=1
        }
        
    }
    if (nums[n-1]!=0){
        nums[j]=nums[n-1]
        j+=1
    }
    while(j<n){
        nums[j]=0
        j+=1
    }
    
    return nums
};