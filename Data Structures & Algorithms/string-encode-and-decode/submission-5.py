class Solution:

    def encode(self, strs: List[str]) -> str:
        #change each to ord of char
        #seperate letter with comman
        #seperate word with full stop
        res = ''
        for s in strs:
            for c in s:
                res += str(ord(c))
                res += ','
            res += '.'
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        char_buff = ''
        word_buff = ''
        for c in s:
            #once we hit a comma we take what is in char_buff and convert to char then put it into word _buff
            if c == ",":
                word_buff += chr(int(char_buff))
                #reset char_buff
                char_buff = ''
            #when we hit full stop we append whats in word_buff and reset
            elif c == ".":
                res.append(word_buff)
                word_buff = ''
            else:
                char_buff += c

        return res
