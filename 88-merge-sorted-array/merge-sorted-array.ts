/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let pointer1 = m-1;
    let pointer2 = n-1;
    let i = m+n-1;
    
    while (pointer2 >= 0) {
        if (pointer1 >= 0 && nums1[pointer1] > nums2[pointer2]) {
            nums1[i] = nums1[pointer1];
            pointer1--;
        } else {
            nums1[i] = nums2[pointer2];
            pointer2--;
        }
        i--;
    }
};