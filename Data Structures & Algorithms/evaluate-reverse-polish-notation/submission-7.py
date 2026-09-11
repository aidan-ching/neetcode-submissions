class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #if numbers place on to the stack
        #if not numbers thats the operation, remove top and do operation with that new Top

        stack = []

        for token in tokens:
            print(stack)
            try:
                stack.append(int(token))
            except:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    
                    stack.append(math.floor(a/b) if a/b>0 else math.ceil(a/b))

        return stack[-1]
                

        