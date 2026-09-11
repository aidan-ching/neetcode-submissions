class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        s = s.toLowerCase();

        let l = 0;
        let r = s.length-1;

        const accepted = "abcdefghijklmnopqrstuvwxyz1234567890"
        const acceptedSet = new Set();

        for (let char of accepted){
            acceptedSet.add(char);
        }





        while (l<r){
            while (l<r && !acceptedSet.has(s[l])){
                l++;
            }
            while (l<r && !acceptedSet.has(s[r])){
                r--;
            }
            if (s[l] !== s[r]){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
