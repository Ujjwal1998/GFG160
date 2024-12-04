class Solution {
    // Function to find the majority elements in the array
    findMajority(arr) {
        // Your code goes here
        const n = arr.length;
        const cutoff = n % 3 === 0 ? n / 3 + 1 : Math.ceil(n / 3);
        let res = new Set();
        let map = new Map();
        for (let num of arr) {
            if (!map.has(num)) map.set(num, 0);
            map.set(num, map.get(num) + 1);
            if (map.get(num) >= cutoff) res.add(num);
        }
        return Array.from(res).sort((a, b) => a - b);
        // T:O(N log N) S:O(N);
    }
    findMajoritySame(arr) {
        // Your code goes here
        const n = arr.length;
        const cutoff = n % 3 === 0 ? n / 3 + 1 : Math.ceil(n / 3);
        let res = new Set();
        let map = new Map();
        for (let num of arr) {
            if (!map.has(num)) map.set(num, 0);
            map.set(num, map.get(num) + 1);
            if (map.get(num) >= cutoff) res.add(num);
        }
        const resArr = Array.from(res)
        if (resArr.length === 2 && resArr[0] > resArr[1]) {
            [resArr[0], resArr[1]] = [resArr[1], resArr[0]];
        }
        return resArr;
        // T:O(N) S:O(N);
    }

    findMajorityBetter(arr) {
        // Your code goes here
        const n = arr.length;
        const cutoff = n % 3 === 0 ? n / 3 + 1 : Math.ceil(n / 3);
        let map = new Map();
        let res = [];
        for (let num of arr) {
            if (!map.has(num)) map.set(num, 0);
            map.set(num, map.get(num) + 1);
        }
        for (let [key, val] of map.entries()) {
            if (val >= cutoff) res.push(key);
        }
        if (res.length === 2 && res[0] > res[1]) {
            [res[0], res[1]] = [res[1], res[0]];
        }
        return res;
        // T:O(N) S:O(N)(no set);
    }

    findMajorityOptimal(arr) {
        // Your code goes here
        const n = arr.length;
        let elem1 = -1;
        let elem2 = -1;
        let cnt1 = 0;
        let cnt2 = 0;
        for (let num of arr) {
            if (num === elem1) cnt1++;
            else if (num === elem2) cnt2++;
            else if (cnt1 === 0) {
                elem1 = num;
                cnt1++;
            }
            else if (cnt2 === 0) {
                elem2 = num;
                cnt2++;
            }else{
                cnt1--;
                cnt2--;
            }
        }
        let res = [];
        cnt1 = 0, cnt2 = 0;
        for (let num of arr) {
            if (num === elem1) cnt1++;
            if (num === elem2) cnt2++;
        }
        if (cnt1 > n / 3) res.push(elem1);
        if (cnt2 > n / 3 && elem1 != elem2) res.push(elem2);

        if (res.length === 2 && res[0] > res[1]) {
            [res[0], res[1]] = [res[1], res[0]];
        }
        return res;
    }
}

const sol = new Solution();
console.log(sol.findMajorityOptimal([-5,3,-5]));