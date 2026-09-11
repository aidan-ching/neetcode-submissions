class Solution:

    #we ascii everything.
    #use "a" to denote next char
    #use "b" to denote next word, new word to append to array

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            for char in word:
                ans+=str(ord(char))
                ans+="a"

            ans+="b"
        return ans



    def decode(self, s: str) -> List[str]:
        solution = []
        word = ""
        letter = ""
        for i in range(len(s)):
            if s[i] == "a": #we can create the letter
                word += chr(int(letter))
                letter = ""
            elif s[i] == "b":
                solution.append(word)
                word = ""
            else:
                letter += s[i]

        return solution









