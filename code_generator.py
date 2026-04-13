# Improved Code Generator from Three Address Code (TAC)

class CodeGenerator:
    def __init__(self, tac):
        self.tac = tac
        self.registers = ["R0", "R1", "R2"]
        self.reg_index = 0

    # Get next register (simple allocation)
    def get_reg(self):
        reg = self.registers[self.reg_index]
        self.reg_index = (self.reg_index + 1) % len(self.registers)
        return reg

    # Generate target code
    def generate(self):
        print("\n--- Generated Target Code ---")

        for stmt in self.tac:
            left, right = stmt.split('=')
            left = left.strip()
            right = right.strip()

            tokens = right.split()

            # Case 1: Binary operation
            if len(tokens) == 3:
                op1, op, op2 = tokens
                reg = self.get_reg()

                print(f"MOV {reg}, {op1}")

                if op == '+':
                    print(f"ADD {reg}, {op2}")
                elif op == '-':
                    print(f"SUB {reg}, {op2}")
                elif op == '*':
                    print(f"MUL {reg}, {op2}")
                elif op == '/':
                    print(f"DIV {reg}, {op2}")

                print(f"MOV {left}, {reg}")

            # Case 2: Unary minus (e.g., t1 = -a)
            elif len(tokens) == 2:
                op, val = tokens
                reg = self.get_reg()

                print(f"MOV {reg}, {val}")
                if op == '-':
                    print(f"NEG {reg}")

                print(f"MOV {left}, {reg}")

            # Case 3: Direct assignment
            else:
                reg = self.get_reg()
                print(f"MOV {reg}, {tokens[0]}")
                print(f"MOV {left}, {reg}")


# Main Program
if __name__ == "__main__":
    # Example TAC
    tac = [
        "t1 = a + b",
        "t2 = t1 * c",
        "t3 = - t2",
        "t4 = t3 / d",
        "x = t4"
    ]

    cg = CodeGenerator(tac)
    cg.generate()
