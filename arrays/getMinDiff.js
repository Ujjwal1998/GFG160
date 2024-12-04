class Solution {
    // Function to get the minimum difference between the heights.
    getMinDiff(arr, k) {
        // your code here
        arr.sort((a,b) => a-b);
        let res = arr[arr.length - 1] - arr[0];
        for(let i = 1; i < arr.length; i++){
            if(arr[i] < k) continue;
            let newMin = Math.min(arr[0]+k, arr[i] - k);
            let newMax = Math.max(arr[arr.length - 1] - k, arr[i-1] + k)
            res = Math.min(res, newMax - newMin)
        }
        return res;
    }
}
