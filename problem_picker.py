import random, sympy
from tex_generator import equationText, factorizeText, drawGraphText, simplifyFracText
import mathematics

x, y = sympy.symbols('x y')

# write n problems of a set type
def generateProblems(n, type):

    # select function and accompanying text based on problem type
    match type:
        case "algebraic equation":
            problemText = equationText
            problemFunction = mathematics.algebraicEquation
        case "trigonometric equation":
            problemText = equationText
            problemFunction = mathematics.trigEqMix
        case "factorize":
            problemText = factorizeText
            problemFunction = mathematics.factorizeEx
        case "linear function":
            problemText = drawGraphText
            problemFunction = mathematics.linearFunc
        case "quadratic function":
            problemText = drawGraphText
            problemFunction = mathematics.quadraticFunc
        case "hyperbola function":
            problemText = drawGraphText
            problemFunction = mathematics.hyperbolaFunc
        case "trigonometric function":
            problemText = drawGraphText
            problemFunction = mathematics.trigFunc
        case "simplify fraction":
            problemText = simplifyFracText
            problemFunction = mathematics.simplifyFracEx

    string = r"        \item " + problemText + "\n"
    string = string + r"    \begin{enumerate}" + "\n"

    # write n number of problems
    for i in range(n):
        string = string + r"        \item $" + problemFunction() +"$" "\n"

    string = string + r"    \end{enumerate}" + "\n"
    return string
