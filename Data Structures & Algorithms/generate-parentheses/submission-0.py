class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #we either add one or we close the previous one
        if n == 0:
            return []

        res = []
        def dfs(string, open, close):
            if open == 0 and close == 0:
                res.append(string)
                return

            else:
                if close == open:
                    #that means we can only open for the next one
                    
                    dfs(string+"(", open-1, close)
                elif open < close and open > 0:
                    #we can either close or open
                    dfs(string+"(", open-1, close)
                    dfs(string+")", open, close-1)
                else:
                    #we can only close
                    dfs(string+")", open, close-1)

        dfs("(", n-1, n)
        return res


        