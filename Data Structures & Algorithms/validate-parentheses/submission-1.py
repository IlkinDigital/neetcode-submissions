class Solution:
    def opp(self, c):
        if c == '(':
            return ')'
        elif c == ')':
            return '('
        elif c == '{':
            return '}' 
        elif c == '}':
            return '{'
        elif c == '[':
            return ']'
        elif c == ']':
            return '['

        return '!'   
    
    def is_open(self, c):
        return c == '(' or c == '[' or c == '{'
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if len(stack) == 0:
                stack.append(c)
                continue
            if self.is_open(stack[-1]) and stack[-1] == self.opp(c):
                stack.pop()
            elif self.is_open(stack[-1]) and not self.is_open(c):
                return False
            else:
                stack.append(c)
        
        return len(stack) == 0
