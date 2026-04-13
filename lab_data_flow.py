# Data Flow Analysis - Live Variable Analysis

class DataFlow:
    def __init__(self, statements):
        self.statements = statements
        self.n = len(statements)
        self.IN = [set() for _ in range(self.n)]
        self.OUT = [set() for _ in range(self.n)]
        self.USE = []
        self.DEF = []

        self.compute_use_def()

    # Compute USE and DEF sets
    def compute_use_def(self):
        for stmt in self.statements:
            parts = stmt.split('=')
            left = parts[0].strip()
            right = parts[1].strip()

            def_set = {left}
            use_set = set()

            for ch in right:
                if ch.isalpha():
                    use_set.add(ch)

            self.DEF.append(def_set)
            self.USE.append(use_set)

    # Perform Live Variable Analysis
    def analyze(self):
        changed = True

        while changed:
            changed = False

            for i in range(self.n - 1, -1, -1):
                old_in = self.IN[i].copy()
                old_out = self.OUT[i].copy()

                # OUT[i] = IN[i+1]
                if i < self.n - 1:
                    self.OUT[i] = self.IN[i + 1]

                # IN[i] = USE[i] ∪ (OUT[i] - DEF[i])
                self.IN[i] = self.USE[i].union(self.OUT[i] - self.DEF[i])

                if old_in != self.IN[i] or old_out != self.OUT[i]:
                    changed = True

    # Display results
    def display(self):
        print("\n--- Data Flow Analysis (Live Variables) ---")
        print(f"{'Stmt':<15} {'USE':<10} {'DEF':<10} {'IN':<15} {'OUT':<15}")

        for i in range(self.n):
            print(f"{self.statements[i]:<15} "
                  f"{str(self.USE[i]):<10} "
                  f"{str(self.DEF[i]):<10} "
                  f"{str(self.IN[i]):<15} "
                  f"{str(self.OUT[i]):<15}")


# Main Program
if __name__ == "__main__":
    # Example statements
    statements = [
        "a = b + c",
        "b = a - d",
        "c = b + e"
    ]

    df = DataFlow(statements)
    df.analyze()
    df.display()
