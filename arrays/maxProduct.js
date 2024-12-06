class Solution {
    maxProduct(arr) {
        // code here
        let max = arr[0];
        for(let i = 0; i < arr.length- 1; i++){
            let currProd = arr[i];
            max = Math.max(currProd, max);
            for(let j = i + 1; j < arr.length; j++){
                currProd = arr[j] * currProd;
                max = Math.max(currProd, max);
            }
        }
        return max;
    }
}
