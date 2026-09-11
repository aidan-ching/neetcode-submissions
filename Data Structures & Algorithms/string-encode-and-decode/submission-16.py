class Solution:

    def encode(self, strs: List[str]) -> str:
        #change each char to their ascii code
        #a to signify char end
        #b to signify word end

        res = ''
        for s in strs:
            for c in s:
                res += str(ord(c))
                res += 'a'
            res += 'b'
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr = ''
        buff = ''
        for c in s:
            if c == 'a': # char ends, buff -> curr
                print(buff)
                curr += chr(int(buff))
                buff = ''
            elif c == 'b': # word ends, curr -> res
                res.append(curr)
                curr = ''
            else:
                buff += c

        return res
