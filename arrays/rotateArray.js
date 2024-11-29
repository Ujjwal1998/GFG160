class Solution {
    // Function to rotate an array by d elements in counter-clockwise direction.
    rotateArr(arr, d) {
        // code here
        const n = arr.length;
        d = d % n
        reverse(arr,0,d-1);
        reverse(arr,d,n-1);
        reverse(arr,0,n-1);
        return arr;
        function reverse(arr, start,end){
            while(start <= end){
                [arr[start], arr[end]] = [arr[end], arr[start]];
                start++;
                end--;
            }
            return arr;
        }
    }
}
