from sympy.parsing.sympy_parser import parse_expr
def to_cnf(expression,t):
    temp = list(expression)
    if t == "f" and "-" in temp and ">" in temp:
        idx = temp.index("-")
        temp[idx] = "|"
        temp.insert(idx,")")
        temp.remove(">")
        temp.insert(0, "~(")
    if (t == "q") : 
        temp.insert(0, "~(")
        temp.append(")")
        if "-" in temp and ">" in temp :
            temp.insert(1, "~(")
            idx = temp.index("-")
            temp[idx] = ")|"
            temp.remove(">")

    cnf = "".join(temp)
    print("CNF : ", cnf)
    simplified_expression = simplify_logic_expression(cnf)
    print("Simplified expression:", simplified_expression)

    return simplified_expression

def simplify_logic_expression(expression):
    parsed_expr = parse_expr(expression)
    simplified_expr = parsed_expr.simplify()
    return str(simplified_expr)