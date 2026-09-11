class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        //Math.min(heights[l], heights[r]) * (r-l)

        let l = 0;
        let r = heights.length-1;
        let max = 0;

        while (l<r){
            let area = Math.min(heights[l], heights[r]) * (r-l);
            if (area > max){
                max = area;
            }

            //we go to the larger of the next ones

            if (heights[l] < heights[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return max;

    }
}
