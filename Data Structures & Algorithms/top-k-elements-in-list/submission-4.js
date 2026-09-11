class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        // count using a hashmap first.

        // create 2d array length of original arr

        const counter = new Map();

        const arr = new Array();

        for (let i = 0; i < nums.length+1; ++i){
            arr.push([])
        }

        for (let n of nums){
            if (counter.has(n)){
                counter.set(n, counter.get(n)+1);
            }
            else{
                counter.set(n, 1);
            }
        }

        for (var [key, val] of counter){
            arr[val].push(key);
        }


        const res = new Array();
        for (let i = arr.length-1; i >= 0; i--){
            for (let n of arr[i]){
                res.push(n);
                k--;
                if (k === 0){
                    return res;
                }
            }
        }
    }
}
