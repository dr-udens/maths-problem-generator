from problem_picker import generateAlgebraicEq, generateTrigEq
from tex_generator import writeTex
import os

# generate the problems
problems = generateAlgebraicEq(4) + generateTrigEq(2)

# put it into LaTeX file
writeTex(problems)

# generate pdf and delete all auxillary files
os.system("pdflatex problem_set.tex")
os.remove("problem_set.log")
os.remove("problem_set.aux")