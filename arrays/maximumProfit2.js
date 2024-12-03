class Solution {
    // Function to find the maximum profit.
    maximumProfit(prices) {
        // your code here
        let max = 0;
        let buy = prices[0];
        for(let i = 0; i < prices.length; i++){
            if(prices[i] < buy){
                buy = prices[i];
            }
            max = Math.max(max, prices[i] - buy);
        }
        return max;
    }
}
