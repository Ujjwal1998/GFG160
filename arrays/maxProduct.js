class Solution {
  maxProduct(arr) {
    // code here
    let max = arr[0];
    for (let i = 0; i < arr.length - 1; i++) {
      let currProd = arr[i];
      max = Math.max(currProd, max);
      for (let j = i + 1; j < arr.length; j++) {
        currProd = arr[j] * currProd;
        max = Math.max(currProd, max);
      }
    }
    return max;
  }
  maxProductOptimal(arr) {
    let leftProduct = 1;
    let rightProduct = 1;
    let left = 0,
      right = arr.length - 1;
    let maxProduct = -Infinity;
    while (left < arr.length) {
      if (leftProduct === 0) leftProduct = 1;
      if (rightProduct === 0) rightProduct = 1;
      leftProduct *= arr[left];
      rightProduct *= arr[right];
      maxProduct = Math.max(maxProduct, leftProduct, rightProduct);
      console.log("left", leftProduct);
      console.log("right", rightProduct);
      //   console.log("max", maxProduct);
      left++;
      right--;
    }
  }
}
const sol = new Solution();
sol.maxProductOptimal([-2, 6, -3, 10, 0, 2]);
