class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const sMap = new Map();
        const tMap = new Map();

        for (const char of s){
            if (sMap.has(char)){
                sMap.set(char, sMap.get(char)+1);
            }
            else{
                sMap.set(char, 1);
            }
        }

        for (const char of t){
            if (tMap.has(char)){
                tMap.set(char, tMap.get(char)+1);
            }
            else{
                tMap.set(char,1);
            }
        }

        //if lengths are different its false anyway
        if (sMap.size != tMap.size){
            return false;
        }


        for (var [key, val] of sMap){
            //if it doesnt exist on tMap return False, or if its the wrong val
            if (!tMap.has(key) || tMap.get(key) != val){
                return false
            }
        }

        return true
    }
}
