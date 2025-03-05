class Solution:
    def simplifyPath(self, path: str) -> str:
        file_name = path.split('/')
        stack = []
        
        for name in file_name:
            if name == '.':
                continue
            if name == '..':
                if stack:
                    stack.pop()
            else:
                if name:
                    stack.append(name)

        
        return '/' + '/'.join(stack)


        