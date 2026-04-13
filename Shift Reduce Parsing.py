a = ""
ac = ""
stk = ""
act = ""
k = z = i = j = c = 0


def check():
    global stk, a, c, i, j
    ac = "REDUCE TO E"

    z = 0
    while z < c:
        # E -> id
        if z + 1 < len(stk) and stk[z] == 'i' and stk[z + 1] == 'd':
            stk = stk[:z] + 'E'
            print(f"${stk}\t{a}$\t{ac}")
            j += 1

        # E -> E+E
        elif z + 2 < len(stk) and stk[z] == 'E' and stk[z + 1] == '+' and stk[z + 2] == 'E':
            stk = stk[:z] + 'E'
            print(f"${stk}\t{a}$\t{ac}")
            i -= 2

        # E -> E*E
        elif z + 2 < len(stk) and stk[z] == 'E' and stk[z + 1] == '*' and stk[z + 2] == 'E':
            stk = stk[:z] + 'E'
            print(f"${stk}\t{a}$\t{ac}")
            i -= 2

        # E -> (E)
        elif z + 2 < len(stk) and stk[z] == '(' and stk[z + 1] == 'E' and stk[z + 2] == ')':
            stk = stk[:z] + 'E'
            print(f"${stk}\t{a}$\t{ac}")
            i -= 2

        z += 1


# Main program
print("GRAMMAR is E->E+E \n E->E*E \n E->(E) \n E->id")
a = input("Enter input string: ")

c = len(a)
act = "SHIFT->"
stk = ""

print("stack \t input \t action")

j = 0
i = 0

while j < c:
    # Check for 'id'
    if j + 1 < c and a[j] == 'i' and a[j + 1] == 'd':
        stk += "id"
        a = a[:j] + "  " + a[j+2:]
        print(f"\n${stk}\t{a}$\t{act}id")
        check()
        j += 2
    else:
        stk += a[j]
        a = a[:j] + " " + a[j+1:]
        print(f"\n${stk}\t{a}$\t{act}symbol")
        check()
        j += 1
