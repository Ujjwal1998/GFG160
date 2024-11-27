class Solution {
    pushZerosToEnd(arr) {
        // code here
        let slow = 0;
        for(let fast = 0; fast < arr.length; fast++){
                if(arr[fast] !== 0){
                    [arr[slow],arr[fast]] = [arr[fast],arr[slow]]
                    slow++;
                }
        }
        return arr;
    }
}