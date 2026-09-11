class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        //a represents new char
        //b represents new word
        let res = "";
        for (let s of strs){
            for (let i in s){
                res += String(s.charCodeAt(i));
                res += 'a'
            }
            res += 'b'
        }
        return res;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const res = new Array();

        let wordBuff = "";
        let charBuff = "";

        for (let c of str){
            if (c === 'a'){ //move charBuff into wordBuff and reset charBuff
                //convert charBuff into num
                wordBuff += String.fromCharCode(Number(charBuff));
                charBuff = "";
            }
            else if (c === 'b'){ //move wordBuff into res and reset wordBuff
                res.push(wordBuff);
                wordBuff = "";
            }
            else{ //number
                charBuff += c;
            }
        }

        return res;


    }
}
