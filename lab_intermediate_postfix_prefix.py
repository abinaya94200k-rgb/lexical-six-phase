# Program to convert Infix to Postfix and Prefix

class ExpressionConversion:

    # Operator precedence
    def precedence(self, op):
        if op in ('+', '-'):
            return 1
        elif op in ('*', '/'):
            return 2
        elif op == '^':
            return 3
        return 0

    # Check operator
    def is_operator(self, c):
        return c in "+-*/^"

    # Infix to Postfix
    def infix_to_postfix(self, expr):
        stack = []
        output = []

        for ch in expr:
            # Operand
            if ch.isalnum():
                output.append(ch)

            # Left bracket
            elif ch == '(':
                stack.append(ch)

            # Right bracket
            elif ch == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # remove '('

            # Operator
            else:
                while (stack and 
                       self.precedence(stack[-1]) >= self.precedence(ch)):
                    output.append(stack.pop())
                stack.append(ch)

        # Pop remaining
        while stack:
            output.append(stack.pop())

        return "".join(output)

    # Infix to Prefix
    def infix_to_prefix(self, expr):
        # Reverse expression
        expr = expr[::-1]

        # Swap brackets
        expr = list(expr)
        for i in range(len(expr)):
            if expr[i] == '(':
                expr[i] = ')'
            elif expr[i] == ')':
                expr[i] = '('

        expr = "".join(expr)

        # Convert to postfix
        postfix = self.infix_to_postfix(expr)

        # Reverse postfix → prefix
        return postfix[::-1]


# Main Program
if __name__ == "__main__":
    ec = ExpressionConversion()

    expr = "a+b*(c-d)"

    print("Infix Expression :", expr)
    print("Postfix Expression :", ec.infix_to_postfix(expr))
    print("Prefix Expression  :", ec.infix_to_prefix(expr))
