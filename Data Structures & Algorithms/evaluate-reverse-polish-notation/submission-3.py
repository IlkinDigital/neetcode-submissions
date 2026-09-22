class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = deque()

        for i in range(len(tokens)):
            t = tokens[i]
            if t == "+" or t == "-" or t == "*" or t == "/":
                b = stack.pop()
                a = stack.pop()
                
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(t))

        return stack[-1]
            