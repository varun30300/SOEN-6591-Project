from sympy.logic.boolalg import Or, And, Not
from sympy.parsing.sympy_parser import parse_expr

def simplify_logic_expression(expression):
    parsed_expr = parse_expr(expression)
    simplified_expr = parsed_expr.simplify()
    return str(simplified_expr)

if __name__ == "__main__":
    try:
        input_expression = input("Enter the logic equation: ")
        simplified_expression = simplify_logic_expression(input_expression)
        print("Simplified expression:", simplified_expression)

    except Exception as e:
        print("Error:", e)
