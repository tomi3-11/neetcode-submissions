class Solution:
    def isValid(self, s: str) -> bool:
        """
        1. Get the length of the string
        2. create an empty stack
        3. loop through the string
        4. if the string contains an open parenthesis then add it to the stack
        5. if stack contains closed brackets then pop the corressponding bracket
        6. if the stack is empty then return True else False
        """

        n = len(s)

        stack = []

        for c in s:
            if c == '{' or c == '(' or c=='[':
                stack.append(c)
            else:

                if not stack: return False

                top = stack[-1]
                if ((c==')' and top != '(') or
                    (c=='}' and top != '{') or
                    (c==']' and top != '[')):
                    return False

                stack.pop()

        return not stack