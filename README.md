# Math problem generator
## Generate equations, graphs and algebra problems
A python project that generates algebra and trigonometry problems according to the users specifications about the method of solving. Problem sets are formatted using LaTeX and the end result is a nice pdf.

Currently it can generate
* expressions to be factorized by using a common factor, grouping like terms, or by using the formula $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$
* algebraic equations that can be solved by factoring, substitution or by plotting the graph of both functions
* trigonometric equations of the forms $\sin(x)=a$, $k \sin(ax+b)=c$, and equations that require substitution (or sometimes factorization).
* formulas of graphs with transformations for linear, quadratic, trigonometric and hyperbola functions
* fractions that can be simplified

### Requirements
* Python 3.1
* SymPy
* LaTeX

## User instructions

In file user_input.py set the variable problems to all the problem sets you wish to have in your file and run it. An example has already been provided in user_input.py.

If you wish to change the title and author of the document go to tex_generator.py and set the variables `author` and `title` to the desired author and title.

### Problem generating function
`generateProblems(n,type)` generates a set of $n$ problems of a set type. $n$ must be an integer and type must be one of these strings: 
* `"algebraic equation"`
* `"trigonometric equation"`
* `"factorize"`
* `"linear function"`
* `"quadratic function"`
* `"hyperbola function"`
* `"trigonometric function"`
* `"simplify fraction"`

### Language
The language used in the finished pdf is Latvian. If you wish to change this simply open tex_generator.py and change the relevant text for problems to English. It also uses babel package in Latvian. If your document is in English, you may simply comment out the line `\usepackage[""" + language + r"""]{babel}`