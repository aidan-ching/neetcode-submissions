class Solution:

    def encode(self, strs: List[str]) -> str:
        #change everyhting to the ord, one big string
        # new letter are denoted as ","
        # new word is denoted as "."

        res = ""
        for s in strs:
            for c in s:
                res += str(ord(c))
                res += ','
            res += "."

        return res
    def decode(self, s: str) -> List[str]:
        #need 2 buffers, one for getting letter
        # one for getting word
        letter_buff = ''
        word_buff = ''
        res = []

        #loop through string, if we hit "," add the int within letter_buff to word buff
        #if we hit ".", add word in word_buff to res

        for char in s:
            if char == ",":
                word_buff += chr(int(letter_buff))
                letter_buff = ''
                continue
            if char == ".":
                res.append(word_buff)
                word_buff = ''
                continue
            letter_buff += char

        return res
            

