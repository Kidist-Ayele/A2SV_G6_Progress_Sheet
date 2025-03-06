class Solution:
    def operation(self, char, a, b):
        a, b = int(a), int(b)
        result = 0
        if char == '+':
            result = a + b
        elif char == '*':
            result = a * b
        elif char == '-':
            result = a - b
        else:
            result = a / b
        return result


    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = set(['*', '/', '+', '-'])

        for char in tokens:
            if char not in operator:
                stack.append(char)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.operation(char, a, b))

        return int(stack[-1])
