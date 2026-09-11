class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    #createKey(s){
        const key = new Array(26).fill(0);

        for (let i = 0; i < s.length; ++i){
            key[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
        }

        return key.toString();
    }

    groupAnagrams(strs) {
        const m = new Map();
        const res = new Array();
        for (let s of strs){
            let key = this.#createKey(s);
            if (!m.has(key)) m.set(key, [s]);
            else m.set(key, [...m.get(key), s]);
        }

        for (let [key, val] of m){
            res.push(val);
        }
        return res
    }
}
