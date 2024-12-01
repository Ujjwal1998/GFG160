class Solution {
    // Function to find the majority elements in the array
    findMajority(arr) {
        // Your code goes here
        const n = arr.length;
        const cutoff = n % 3 === 0 ? n/3 + 1 : Math.ceil(n/3);
        let res = new Set();
        let map = new Map();
        for(let num of arr){
            if(!map.has(num)) map.set(num, 0);
            map.set(num, map.get(num) + 1);
            if(map.get(num) >= cutoff) res.add(num);
        }
        return Array.from(res).sort((a,b)=> a - b);
    }
}
