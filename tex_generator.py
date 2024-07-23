# texts for problems
author = "darida udens" # author name
title = "Uzdevumi" # title of document

equationText = "Atrisini vienādojumu." # text for solving equations
factorizeText = "Sadali izteiksmi reizinātājos." # text for factorizing an expression
drawGraphText = "Uzzīmē funkcijas grafiku." # text for drawing the graph of a function
simplifyFracText = "Saīsini doto daļu." # text for simplifying a fraction

# LaTeX settings
language = "latvian" # language for LaTeX babel package

# necessary text
beginning = r"""
\documentclass[12pt]{article}
\usepackage{enumitem}
\usepackage[""" + language + r"""]{babel}
 
\setlength\parindent{0pt}
\author{""" + author + r"""}
\date{\today}
\title{""" + title + r"""}
 
\begin{document}
    \maketitle
    \begin{enumerate}
"""
end = r"""
	\end{enumerate}
\end{document}
"""
# function for writing the tex document
def writeTex(problems):
    with open("problem_set.tex","w", encoding="utf-8") as file:
        file.write(beginning)
        file.write(problems)
        file.write(end)
