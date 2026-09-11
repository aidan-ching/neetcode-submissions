class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        //check target-curr on hashmap, insert if missing, return curr, and hashmap[target-curr] if found
        const m = new Map();
        
        for (let i = 0; i < nums.length; ++i){
            if (m.has(target-nums[i])){
                return [i, m.get(target-nums[i])];
            }
            m.set(nums[i], i);
        }

    }
}
