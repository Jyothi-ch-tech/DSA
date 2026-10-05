class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in s:
            if i=='(':
                stack.append(0)
            else:
                inner=stack.pop()
                if inner==0:
                    stack.append(stack.pop()+1)
                else:
                    stack.append(stack.pop()+2*inner)
        return stack.pop()
        