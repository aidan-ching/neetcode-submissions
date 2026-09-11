class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if (nums.length === 0){
            return 0;
        }


        //convert to set

        const s = new Set();

        for (let n of nums){
            s.add(n);
        }

        //loop through the set values, and iterate only if there is no val that is lower. 
        let max_length = 1;


        for (let val of nums){
            
            let offset = 1;
            if (!s.has(val-1)){
                while (s.has(val+offset)){
                    if (offset+1 > max_length){
                        max_length = offset+1;
                    } 
                    offset += 1;
                }
            }
        }
        return max_length;


    }
}
