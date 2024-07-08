# Math problem generator
## Generate equations, graphs and algebra problems
A python project that generates algebra and trigonometry problems according to the users specifications about the method of solving. Problem sets are formatted using LaTeX and the end result is a nice pdf.

Currently it can generate
* algebraic equations that can be solved by factoring, substitution or by plotting the graph of both functions
* trigonometric equations of the forms $\sin(x)=a$, $k \sin(ax+b)=c$, and equations that require substitution (or sometimes factorization).

### Requirements
* Python 3.1
* SymPy
* LaTeX

## User instructions

In file user_input.py set the variable problems to all the problem sets you wish to have in your file and run it. An example has already been provided in user_input.py.

If you wish to change the title and author of the document go to tex_generator.py and set the variables `author` and `title` to the desired author and title.

### Problem generating functions

1. `generateAlgebraicEq(n)` generates n algebraic equations.
2. `generateTrigEq(n)` generates n trigonometric equations.

### Language
The language used in the finished pdf is Latvian. If you wish to change this simply open tex_generator.py and change the relevant text to English. It also uses babel package in Latvian. If your document is in English, you may simply comment out the line `\usepackage[""" + language + r"""]{babel}`
