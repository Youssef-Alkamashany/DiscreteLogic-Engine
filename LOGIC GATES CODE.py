import itertools

def to_tf(val):
    return "T" if val else "F"

def print_detailed_tf_proof():
    print("\nDETAILED PROOF TABLE (T/F)")
    print("-" * 165)

    header = "| A | B | C | D | A^B | C.D | (Imp)-> | LHS(=) | ~C | ~D | ~C v ~D | RHS | Equiv |"
    print(header)
    print("-" * 165)

    combinations = list(itertools.product([0, 1], repeat=4))

    for combo in combinations:
        A, B, C, D = combo

        xor_ab = 1 if (A != B) else 0
        and_cd = 1 if (C and D) else 0

        if xor_ab == 1 and and_cd == 0:
            imp_res = 0
        else:
            imp_res = 1

        lhs_final = 1 if imp_res == 1 else 0

        not_c = 1 if C == 0 else 0
        not_d = 1 if D == 0 else 0

        not_c_or_not_d = 1 if (not_c or not_d) else 0

        rhs_final = 1 if (xor_ab and not_c_or_not_d) else 0

        match = 1 if (lhs_final == rhs_final) else 0

        print(f"| {to_tf(A)} | {to_tf(B)} | {to_tf(C)} | {to_tf(D)} |  {to_tf(xor_ab)}  |  {to_tf(and_cd)}  |    {to_tf(imp_res)}    |    {to_tf(lhs_final)}    | {to_tf(not_c)}  | {to_tf(not_d)}  |    {to_tf(not_c_or_not_d)}    |  {to_tf(rhs_final)}  |   {to_tf(match)}   |")

    print("-" * 165)

if __name__ == "__main__":
    print_detailed_tf_proof()