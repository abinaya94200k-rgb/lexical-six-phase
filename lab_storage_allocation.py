# Storage Allocation in Compiler Design
# Demonstrates memory allocation for variables

class StorageAllocation:
    def __init__(self):
        self.symbol_table = {}
        self.memory_address = 1000   # starting address

    # Allocate memory for variable
    def allocate(self, var_name, var_type):
        size = self.get_size(var_type)

        if var_name not in self.symbol_table:
            self.symbol_table[var_name] = {
                "type": var_type,
                "address": self.memory_address,
                "size": size
            }
            self.memory_address += size
        else:
            print(f"Variable '{var_name}' already declared!")

    # Return size based on type
    def get_size(self, var_type):
        sizes = {
            "int": 4,
            "float": 8,
            "char": 1,
            "double": 8
        }
        return sizes.get(var_type, 4)  # default size = 4

    # Display Symbol Table
    def display(self):
        print("\n--- Symbol Table (Storage Allocation) ---")
        print(f"{'Variable':<10} {'Type':<10} {'Address':<10} {'Size':<5}")
        for var, details in self.symbol_table.items():
            print(f"{var:<10} {details['type']:<10} {details['address']:<10} {details['size']:<5}")


# Main Program
if __name__ == "__main__":
    sa = StorageAllocation()

    print("Storage Allocation Program\n")

    # Example variables
    sa.allocate("a", "int")
    sa.allocate("b", "float")
    sa.allocate("c", "char")
    sa.allocate("d", "double")

    sa.display()
