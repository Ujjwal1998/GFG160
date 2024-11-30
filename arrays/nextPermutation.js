class Solution {
    nextPermutation(arr) {
        //code here
        const n = arr.length;
        let i = n;
        for (i; i > 0; i--) {
            if (arr[i - 1] < arr[i]) break;
        }
        let pivotIndex = i === 0 ? -1 : i - 1;
        if (pivotIndex === -1) return reverse(pivotIndex + 1, n - 1);
        for (let j = n - 1; j > pivotIndex; j--) {
            if (arr[j] > arr[[pivotIndex]]) {
                [arr[j], arr[pivotIndex]] = [arr[pivotIndex], arr[j]];
                break;
            }
        }
        return reverse(pivotIndex + 1, n - 1);
        function reverse(start, end) {
            while (start < end) {
                [arr[start], arr[end]] = [arr[end], arr[start]];
                start++;
                end--;
            }
            return arr;
        }
    }
}