class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o.lstrip('-').isdigit():   # handles negatives too
                stack.append(int(o))
            elif o == "+":
                stack.append(stack[-1] + stack[-2])
            elif o == "D":
                stack.append(2 * stack[-1])
            elif o == "C":
                stack.pop()

        return sum(stack)