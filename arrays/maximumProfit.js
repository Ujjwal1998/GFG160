class Solution {
    /**
    * @param number[] prices

    * @returns number
    */
    maximumProfit(prices) {
        // code here
        // let res = 0;
        // let idx = 0;
        // const n = prices.length;
        // let localMinima = prices[0];
        // let localMaxima = prices[0];
        // while( idx < n -1){
        //     while(prices[idx] > prices[idx+1] && idx < n - 1){
        //         idx++;
        //     }
        //     localMinima = prices[idx];
        //     while(prices[idx] < prices[idx+1] && idx < n - 1){
        //         idx++;
        //     }
        //     localMaxima = prices[idx];
        //     res += localMaxima - localMinima;
        // }
        // return res;
        // }
        let res = 0;
        const n = prices.length;
        for(let i = 1; i < n; i++){
            if(prices[i] > prices[i-1]){
                res += prices[i] - prices[i-1];
            }
        }
        return res;
    }
}
