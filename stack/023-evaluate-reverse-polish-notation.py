class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                first = int(stack[-1])
                stack.pop()
                second = int(stack[-1])
                stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(second - first)
                elif token == "*":
                    stack.append(first * second)
                else:
                    stack.append(second / first)
            else:
                stack.append(token)

        return int(stack[-1])
