function search(arr, key) {
        // code here
        let lo = 0;
        let hi = arr.length - 1;
        while (lo <= hi){
            let mid = Math.floor((hi + lo) / 2)
            // console.log(arr[mid], key, lo, hi)
            if (arr[mid] == key) return mid;
            if (arr[mid] <= arr[arr.length - 1]){
                if (key > arr[mid] && key <= arr[hi]){
                    lo = mid + 1
                } else{
                    hi = mid - 1
                }
            }else{
                if (key < arr[mid] && key >= arr[lo] ){
                    hi = mid - 1
                } else{
                    lo = mid + 1
                }
            }
        }
        return -1
    }
