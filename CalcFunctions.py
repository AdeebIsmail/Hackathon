
import sympy as simp

x = simp.symbols("x")
eq = simp.parse_expr(input())
def integrals(eq):
    x = simp.symbols("x")
    eq = simp.parse_expr(input())

    return simp.integrate(eq,x)

def derivative(eq):
    x = simp.symbols("x")
    eq = simp.parse_expr(input())
    return simp.diff(eq, x)
