class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const group = new Map();
        for (let s of strs){
            let key = this.#createKey(s);
            if (group.has(key)){
                group.set(key, [...group.get(key), s]);
            }
            else{
                group.set(key, [s]);
            }
        }

        console.log(group)

        return Array.from(group.values())
    }

    #createKey(s){
        const key = new Array(26).fill(0);

        for (let i in s){
            key[s.charCodeAt(i) - 'a'.charCodeAt(0)] = key[s.charCodeAt(i) - 'a'.charCodeAt(0)]+1;
        }
        return key.toString();
    }
}
