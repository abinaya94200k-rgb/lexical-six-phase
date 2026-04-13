from collections import deque

class LR0:
    def __init__(self, grammar):
        self.grammar = grammar
        self.productions = []
        self.states = []
        self.transitions = {}
        self._prepare_grammar()

    # Convert grammar into tuple form (IMPORTANT FIX)
    def _prepare_grammar(self):
        for lhs, rhs_list in self.grammar.items():
            for rhs in rhs_list:
                self.productions.append((lhs, tuple(rhs.split())))

    # Closure operation
    def closure(self, items):
        closure_set = set(items)

        while True:
            new_items = set(closure_set)

            for (lhs, rhs, dot_pos) in closure_set:
                if dot_pos < len(rhs):
                    symbol = rhs[dot_pos]

                    if symbol in self.grammar:
                        for prod in self.grammar[symbol]:
                            new_items.add((symbol, tuple(prod.split()), 0))

            if new_items == closure_set:
                break

            closure_set = new_items

        return frozenset(closure_set)

    # GOTO function
    def goto(self, items, symbol):
        goto_set = set()

        for (lhs, rhs, dot_pos) in items:
            if dot_pos < len(rhs) and rhs[dot_pos] == symbol:
                goto_set.add((lhs, rhs, dot_pos + 1))

        return self.closure(goto_set)

    # Get all grammar symbols
    def _all_symbols(self):
        symbols = set()
        for lhs, rhs in self.productions:
            symbols.add(lhs)
            for sym in rhs:
                symbols.add(sym)
        return symbols

    # Construct Canonical Collection
    def construct_states(self):
        start_prod = self.productions[0]
        start_item = (start_prod[0], start_prod[1], 0)

        start_state = self.closure({start_item})
        self.states.append(start_state)

        queue = deque([start_state])

        while queue:
            state = queue.popleft()

            for symbol in self._all_symbols():
                new_state = self.goto(state, symbol)

                if new_state:
                    if new_state not in self.states:
                        self.states.append(new_state)
                        queue.append(new_state)

                    self.transitions[(self.states.index(state), symbol)] = self.states.index(new_state)

    # Display LR(0) Items
    def display(self):
        print("\n--- LR(0) Item Sets ---")

        for i, state in enumerate(self.states):
            print(f"\nI{i}:")
            for (lhs, rhs, dot) in state:
                rhs_list = list(rhs)
                rhs_list.insert(dot, '.')
                print(f"{lhs} -> {' '.join(rhs_list)}")

        print("\n--- Transitions ---")
        for (state, symbol), target in self.transitions.items():
            print(f"I{state} -- {symbol} --> I{target}")


# Main Program
if __name__ == "__main__":
    grammar = {
        "S'": ["S"],
        "S": ["C C"],
        "C": ["c C", "d"]
    }

    lr0 = LR0(grammar)
    lr0.construct_states()
    lr0.display()
