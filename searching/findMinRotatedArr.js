function findMin(arr) {
        // your code here
        let lo = 0;
        let hi = arr.length - 1;
        let bndry = -1;
        let target = Number.MAX_VALUE;
        while (lo <= hi) {
            let mid = Math.floor((lo + hi) / 2)
            console.log(lo, hi, mid, bndry)
            if (arr[mid] <= arr[arr.length - 1]) {
                console.log("here")
                bndry = arr[mid]
                hi = mid - 1
            }else{
                lo = mid + 1
            }
        }
        console.log(bndry)
        return bndry
    }
findMin([39,45,57,4,24])
