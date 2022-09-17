
import sympy as simp

x = simp.symbols("x")
eq = simp.parse_expr(input())
def integrals(eq):
    return simp.integrate(eq,x)
def derivative(eq):
    return  simp.diff(eq, x)
print(integrals(eq))
print(derivative(eq))