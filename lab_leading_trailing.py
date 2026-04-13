# Program to find LEADING and TRAILING of a grammar

class LeadingTrailing:
    def __init__(self, grammar):
        self.grammar = grammar
        self.leading = {nt: set() for nt in grammar}
        self.trailing = {nt: set() for nt in grammar}

    # Check terminal
    def is_terminal(self, symbol):
        return not symbol.isupper()

    # Compute LEADING
    def compute_leading(self):
        changed = True
        while changed:
            changed = False
            for nt in self.grammar:
                for prod in self.grammar[nt]:
                    symbols = prod.split()

                    # Rule 1: first symbol terminal
                    if self.is_terminal(symbols[0]):
                        if symbols[0] not in self.leading[nt]:
                            self.leading[nt].add(symbols[0])
                            changed = True

                    # Rule 2: first symbol non-terminal
                    else:
                        for sym in self.leading[symbols[0]]:
                            if sym not in self.leading[nt]:
                                self.leading[nt].add(sym)
                                changed = True

    # Compute TRAILING
    def compute_trailing(self):
        changed = True
        while changed:
            changed = False
            for nt in self.grammar:
                for prod in self.grammar[nt]:
                    symbols = prod.split()

                    # Rule 1: last symbol terminal
                    if self.is_terminal(symbols[-1]):
                        if symbols[-1] not in self.trailing[nt]:
                            self.trailing[nt].add(symbols[-1])
                            changed = True

                    # Rule 2: last symbol non-terminal
                    else:
                        for sym in self.trailing[symbols[-1]]:
                            if sym not in self.trailing[nt]:
                                self.trailing[nt].add(sym)
                                changed = True

    # Display results
    def display(self):
        print("\n--- LEADING ---")
        for nt in self.leading:
            print(f"{nt} : {{ {', '.join(self.leading[nt])} }}")

        print("\n--- TRAILING ---")
        for nt in self.trailing:
            print(f"{nt} : {{ {', '.join(self.trailing[nt])} }}")


# Main Program
if __name__ == "__main__":
    # Example Grammar
    # E → E + T | T
    # T → T * F | F
    # F → ( E ) | id

    grammar = {
        "E": ["E + T", "T"],
        "T": ["T * F", "F"],
        "F": ["( E )", "id"]
    }

    lt = LeadingTrailing(grammar)
    lt.compute_leading()
    lt.compute_trailing()
    lt.display()
