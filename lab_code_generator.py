# Simple Code Generator from Three Address Code (TAC)

class CodeGenerator:
    def __init__(self, tac):
        self.tac = tac

    # Generate target code
    def generate(self):
        print("\n--- Generated Target Code ---")

        for stmt in self.tac:
            parts = stmt.split('=')
            left = parts[0].strip()
            right = parts[1].strip()

            tokens = right.split()

            # Case 1: Binary operation
            if len(tokens) == 3:
                op1, op, op2 = tokens

                print(f"MOV R0, {op1}")

                if op == '+':
                    print(f"ADD R0, {op2}")
                elif op == '-':
                    print(f"SUB R0, {op2}")
                elif op == '*':
                    print(f"MUL R0, {op2}")
                elif op == '/':
                    print(f"DIV R0, {op2}")

                print(f"MOV {left}, R0")

            # Case 2: Simple assignment
            else:
                print(f"MOV R0, {tokens[0]}")
                print(f"MOV {left}, R0")


# Main Program
if __name__ == "__main__":
    # Example TAC
    tac = [
        "t1 = a + b",
        "t2 = t1 * c",
        "t3 = t2 - d"
    ]

    cg = CodeGenerator(tac)
    cg.generate()
