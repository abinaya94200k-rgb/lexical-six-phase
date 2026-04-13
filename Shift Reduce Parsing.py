# Corrected Shift Reduce Parsing Program

class ShiftReduceParser:
    def __init__(self, grammar, input_string):
        self.grammar = grammar
        self.input = input_string + '$'
        self.stack = []

    # Try reduction
    def reduce(self):
        for lhs, productions in self.grammar.items():
            for prod in productions:
                prod_len = len(prod)

                if prod_len <= len(self.stack):
                    if ''.join(self.stack[-prod_len:]) == prod:
                        # Perform reduction
                        for _ in range(prod_len):
                            self.stack.pop()
                        self.stack.append(lhs)
                        print(f"Reduce: {prod} -> {lhs}")
                        return True
        return False

    # Parsing process
    def parse(self):
        print(f"{'Stack':<15} {'Input':<15} {'Action'}")

        i = 0
        start_symbol = list(self.grammar.keys())[0]

        while True:
            action_done = False

            # Try reduction as much as possible
            while self.reduce():
                print(f"{''.join(self.stack):<15} {self.input[i:]:<15} Reduce")
                action_done = True

            # Accept condition
            if ''.join(self.stack) == start_symbol and self.input[i:] == '$':
                print(f"{''.join(self.stack):<15} {self.input[i:]:<15} Accept")
                print("\nString Accepted ✅")
                break

            # Shift
            if i < len(self.input):
                self.stack.append(self.input[i])
                print(f"{''.join(self.stack):<15} {self.input[i+1:]:<15} Shift")
                i += 1
                action_done = True

            # If no action possible → reject
            if not action_done:
                print("\nString Rejected ❌")
                break


# Main Program
if __name__ == "__main__":
    # Grammar: S → aSb | ab
    grammar = {
        "S": ["aSb", "ab"]
    }

    input_string = "aabb"

    parser = ShiftReduceParser(grammar, input_string)
    parser.parse()
