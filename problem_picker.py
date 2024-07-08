import random, sympy
from tex_generator import equationText, factorizeText, drawGraphText
from mathematics import algebraicEquation, trigEqMix, factorizeEx

x, y = sympy.symbols('x y')

# write n problems using known text and problem function
def generateProblems(n, problemText, problemFunction):
    string = r"        \item " + problemText + "\n"
    string = string + r"    \begin{enumerate}" + "\n"

    for i in range(n):
        string = string + r"        \item $" + problemFunction() +"$" "\n"

    string = string + r"    \end{enumerate}" + "\n"
    return string

# write as many algebraic equations as specified by n.
def generateAlgebraicEq(n):
    return generateProblems(n, equationText, algebraicEquation)

# write as many trigonometric equations (generic or solved w general methods) as specified by n
def generateTrigEq(n):
    return generateProblems(n, equationText, trigEqMix)

# helper function for getting factorizeEx in the same format as all the Eq functions
def factorizeExEq():
    return sympy.latex(factorizeEx())
# write as many factorization problems ar specified by n
def generateFactorizeEx(n):
    return generateProblems(n, factorizeText, factorizeExEq)