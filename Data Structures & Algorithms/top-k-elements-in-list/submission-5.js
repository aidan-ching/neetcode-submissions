class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        //count using hashmap then place into appropriate places
        const m = new Map();

        for (let n of nums){
            if (!m.has(n)) m.set(n, 1);
            else m.set(n, m.get(n)+1);
        }

        const bucket = new Array(nums.length+1);

        for (let i = 0; i < bucket.length; ++i){
            bucket[i] = new Array();
        }

        for (let [key, val] of m) bucket[val].push(key);


        const res = new Array();


        for (let i = bucket.length-1; i >= 0; i--){
            for (let j = 0; j < bucket[i].length; ++j){
                res.push(bucket[i][j]);
                k--;
                if (k===0) return res;
            }
        }

        
        


    }
}
