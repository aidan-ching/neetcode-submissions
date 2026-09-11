class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        //count both with map
        //compare them manually

        const sMap = new Map();
        const tMap = new Map();

        for (let char of s){
            if (sMap.has(char)){
                sMap.set(char, sMap.get(char)+1);
            }
            else{
                sMap.set(char,1);
            }
        }

        for (let char of t){
            if (tMap.has(char)){
                tMap.set(char, tMap.get(char)+1);
            }
            else{
                tMap.set(char, 1);
            }
        }

        if (sMap.size != tMap.size) return false;

        for (let [key, val] of sMap){
            //return false if it doesnt exist or val is different value
            if (!tMap.has(key) || tMap.get(key) !== val) return false;
        }

        return true;


    }
}
