class Solution {
    // Function to find the sum of contiguous subarray with maximum sum.
    maxSubarraySum(arr) {
        // code here
        let sum = arr[0];
        let max = sum;
        for(let i = 1; i < arr.length; i++){
            sum = Math.max(sum+arr[i],arr[i])
            max = Math.max(max, sum);
        }
        return max;
    }
}
