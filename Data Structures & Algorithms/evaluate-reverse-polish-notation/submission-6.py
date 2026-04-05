class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]

        eval_stack = []

        for token in tokens:
            if token in ops:
                eval_stack.append(evaluate(eval_stack, token))
            else:
                eval_stack.append(int(token))
        return eval_stack[-1]

def evaluate(stack, op) -> int:
    rhs: int = stack.pop()
    lhs: int = stack.pop()

    if op == "+":
        return lhs + rhs
    elif op == "-":
        return lhs - rhs
    elif op == "*":
        return lhs*rhs
    else:
        return int(lhs / rhs)
