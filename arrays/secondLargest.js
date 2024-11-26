class Solution {
    // Function returns the second largest element
    getSecondLargest(arr) {
        let largest = Number.NEGATIVE_INFINITY;
        let secondLargest = Number.NEGATIVE_INFINITY;
        for(let i = 0; i < arr.length; i++){
            let current = arr[i];
            if(current > largest && current > secondLargest){
                secondLargest = largest;
                largest = current;
            }
            if(current < largest && current > secondLargest){
                secondLargest = current;
            }
        }
        return secondLargest === Number.NEGATIVE_INFINITY ? -1 : secondLargest;
    }
}
