from dataclasses import dataclass
from typing import List, Optional

# Define TAC structure
@dataclass
class TAC:
    op: str
    arg1: str
    arg2: Optional[str]
    result: str


class TACRepresentations:
    def __init__(self, code: List[TAC]):
        self.code = code

    # Quadruple Representation
    def print_quadruple(self):
        print("\n--- Quadruple Representation ---")
        print(f"{'OP':<6} {'ARG1':<6} {'ARG2':<6} {'RESULT':<6}")
        for c in self.code:
            print(f"{c.op:<6} {c.arg1:<6} {str(c.arg2):<6} {c.result:<6}")

    # Triple Representation
    def print_triple(self):
        print("\n--- Triple Representation ---")
        print(f"{'ID':<4} {'OP':<6} {'ARG1':<8} {'ARG2':<8}")
        for i, c in enumerate(self.code):
            arg1 = f"({self._find_res(c.arg1)})" if self._is_temp(c.arg1) else c.arg1
            arg2 = f"({self._find_res(c.arg2)})" if self._is_temp(c.arg2) else str(c.arg2)
            print(f"({i})  {c.op:<6} {arg1:<8} {arg2:<8}")

    # Check temporary variable
    def _is_temp(self, var) -> bool:
        return bool(var and str(var).startswith('t'))

    # Find index of result
    def _find_res(self, res) -> int:
        for i, c in enumerate(self.code):
            if c.result == res:
                return i
        return -1


# Main Program
if __name__ == '__main__':
    print("Three Address Code Representation\n")

    # Example Expression:
    # t1 = a - b
    # t2 = t1 * c
    # t3 = t2 + d

    tacs = [
        TAC('-', 'a', 'b', 't1'),
        TAC('*', 't1', 'c', 't2'),
        TAC('+', 't2', 'd', 't3')
    ]

    rep = TACRepresentations(tacs)

    # Print outputs
    rep.print_quadruple()
    rep.print_triple()
