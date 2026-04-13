# DAG Representation for Basic Block Optimization

class Node:
    def __init__(self, op, left=None, right=None, value=None):
        self.op = op          # operator
        self.left = left      # left child
        self.right = right    # right child
        self.value = value    # variable name / constant
        self.labels = []      # variables representing this node


class DAG:
    def __init__(self):
        self.nodes = []

    # Find existing node
    def find_node(self, op, left, right):
        for node in self.nodes:
            if node.op == op and node.left == left and node.right == right:
                return node
        return None

    # Find leaf node
    def get_leaf(self, value):
        for node in self.nodes:
            if node.value == value:
                return node

        new_node = Node(None, value=value)
        new_node.labels.append(value)
        self.nodes.append(new_node)
        return new_node

    # Build DAG
    def build(self, statements):
        for stmt in statements:
            left, right = stmt.split('=')
            left = left.strip()
            right = right.strip()

            parts = right.split()

            # Case: binary operation
            if len(parts) == 3:
                op1, op, op2 = parts

                left_node = self.get_leaf(op1)
                right_node = self.get_leaf(op2)

                existing = self.find_node(op, left_node, right_node)

                if existing:
                    existing.labels.append(left)
                else:
                    new_node = Node(op, left_node, right_node)
                    new_node.labels.append(left)
                    self.nodes.append(new_node)

            # Case: assignment
            else:
                node = self.get_leaf(parts[0])
                node.labels.append(left)

    # Display DAG
    def display(self):
        print("\n--- DAG Nodes ---")
        for i, node in enumerate(self.nodes):
            if node.op:
                print(f"Node {i}: ({node.op}) -> "
                      f"{node.left.value if node.left.value else node.left.labels}, "
                      f"{node.right.value if node.right.value else node.right.labels} "
                      f"| Labels: {node.labels}")
            else:
                print(f"Node {i}: Value = {node.value} | Labels: {node.labels}")


# Main Program
if __name__ == "__main__":
    # Example basic block
    statements = [
        "t1 = a + b",
        "t2 = a + b",
        "t3 = t1 + c",
        "t4 = t2 + c"
    ]

    dag = DAG()
    dag.build(statements)
    dag.display()
