# Math problem generator
## Generate equations, graphs and algebra problems
A python project that generates algebra and trigonometry problems according to the users specifications about the method of solving. Problem sets are formatted using LaTeX and the end result is a nice pdf.

### Requirements
* Python 3.1
* SymPy
* LaTeX

## User instructions

In file user_input.py set the variable problems to all the problem sets you wish to have in your file.

### Problem generating functions

1. generateAlgebraicEq(n) - generates n equations that can be solved either by factoring, substitution or by drawing graphs.
2. generateTrigEq(n) - generates n trigonometric equations. The equations can be solved either in one step, several steps or might require the use of substitution (or sometimes factoring) before they can be solved as classic trigonometric equations.
