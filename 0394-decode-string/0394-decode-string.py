class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            text = []
            number = []
            if char == ']':
                # Extract text in reverse order
                while stack and stack[-1] != '[':
                    text.append(stack.pop())
                stack.pop()

                # Extract number in reverse order
                while stack and stack[-1].isdigit():
                    number.append(stack.pop())

                word = ''.join(text[::-1])
                num = int(''.join(number[::-1]))

                # Append to the stack after the operation
                stack.append(word * num)
            else:
                stack.append(char)

        return ''.join(stack)
                 

        