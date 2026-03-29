class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        last = 0
        path += '/'

        for i in range(1, len(path)):
            if path[i] == '/':
                segment = path[last+1:i]
                last = i

                if segment == "" or segment == ".":
                    continue
                elif segment == ".." and stack:
                    stack.pop()
                elif segment != '..':
                    stack.append(segment)
                    
        return '/' + '/'.join(stack)
        