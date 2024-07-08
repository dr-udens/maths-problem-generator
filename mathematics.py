import random, sympy

x, y = sympy.symbols('x y')

# change the sign of the number w 50% probability
def sign(n):
    a=random.randrange(2)

    if a == 1:
        n = - 1 * n

    return n

# turn expression into equation
def equify(string):
    return string + " = 0"

############################### TOPIC 0 ###############################
# problems that are taught in middle school

# common factor / kopīgais reizinātājs
def commonFacEx():
    # generate random non zero coefficients a and b; n and m - powers of x
    a = sign(random.randrange(1,10))
    b = sign(random.randrange(1,4))
    n = random.randrange(1,4)
    m = random.randrange(1,4)
    
    # generate the expression analytically
    ex = sympy.expand(a * x ** n * (x ** m + b ** m))
    return ex

# grouping / grupēšanas paņēmiens
def groupingEx():
    # random small coefficients
    a = sign(random.randrange(1,4))
    b = sign(random.randrange(1,4))
    c = sign(random.randrange(1,4))
    # generate random DIFFERENT powers of x
    n = random.randrange(1,5)
    m = random.randrange(1,5)
    while n == m:
        m = random.randrange(1,3)

    ex = sympy.expand((a * x ** n + b) * (x ** m + c))
    return ex

# linear function
def linearFunc():
    a = sign(random.randrange(11))
    b = sign(random.randrange(1,6))
    c = sign(random.randrange(6))
    k = random.randrange(2)

    # choose form y = kx + b or Ax + Bx + C based on k
    if k == 0:
        ex = "y = " + sympy.latex(sympy.Rational(a,b) * x + c)
    else:
        ex = sympy.latex(a * x + b * y + c) + " = 0"

    return ex

# graph for quadratic function y = ax^2 + bx + c
def quadraticFunc():
    k = random.randrange(1,4) # this is for denominator for a
    a = sign(random.randrange(1,6))
    b = sign(random.randrange(6))
    c = sign(random.randrange(6))
    return "y = " + sympy.latex(a/k * x ** 2 + b * x + c)

############################### END ###############################

############################### TOPIC 1: VECTORS ###############################
############################### END ###############################

############################### TOPIC 2: LINEAR FUNCTION ###############################
############################### END ###############################

############################### TOPIC 3: COMBINATORICS AND GRAPHS ###############################
############################### END ###############################

############################### TOPIC 4: STATISTICS ###############################
############################### END ###############################

############################### TOPIC 5: EQUATIONS, ALGEBRAIC FRACTIONS AND THEIR GRAPHS ###############################°

# for formula a^3 +/- b^3
def cubeEx():
    # generate two relatively small non zero coefficients for my equations
    a = sign(random.randrange(1,4))
    b = sign(random.randrange(1,5))

    ex = sympy.expand((a * x) ** 3 + b ** 3)
    return ex

# randomly pick one of the three factorizable expression types
def factorizeEx():
    k = random.randrange(3)

    if k == 0:
        return commonFacEx()
    if k == 1:
        return cubeEx()
    if k== 2:
        return groupingEx()

# equation of the form ax^4 + bx^2 + c = 0
def substitution():
    # generate the twoo roots
    a = sign(random.randrange(9))
    b = sign(random.randrange(9))

    return sympy.expand((x ** 2 - a) * (x ** 2 - b))

# simple edge case where students would use graphs to solve the equation
def graphEq():
    a = sign(random.randrange(4))
    b = sign(random.randrange(10))

    # pick the type of edge case - sqrt(x), x^3 or x^4
    k = random.randrange(3)
    if k == 0:
        ex = x ** 3
    if k == 1:
        ex = sympy.sqrt(x)
    if k == 2:
        ex = x ** 4

    return sympy.latex(ex) + " = " + sympy.latex(a * x + b)

# call random type of equation
def algebraicEquation():
    k = random.randrange(3)

    if k == 0:
        return equify(sympy.latex(factorizeEx()))
    if k == 1:
        return equify(sympy.latex(substitution()))
    if k == 2:
        return graphEq()

# graph for algebraic fractions (hyperbola)
def hyperbola():
    k = sign(random.randrange(1,13))
    a = random.randrange(1,3)
    b = sign(random.randrange(6))
    c = sign(random.randrange(6))
    ex = "y = " + sympy.latex(k / (a * x - b) + c)
    return ex
############################### END ###############################

############################### TOPIC 6: EQUATIONS WITH FRACTIONS ###############################
############################### END ###############################

############################### TOPIC 7: SIN AND COS FUNCTIONS ###############################

# pick a root from 0, 1/2, sqrt(2)/2, sqrt(3)/2 and 1 
def trigRoot():
    k = random.randrange(7)
    if k < 3:
        return 0
    if k == 3:
        return sign(sympy.Rational(1,2))
    if k == 4:
        return sign(sympy.sqrt(2)/2)
    if k == 5:
        return sign(sympy.sqrt(3)/2)
    if k == 6:
        return sign(1)

# typical radian value generator
def trigValue():
    k = random.randrange(5)
    if k == 0:
        return 0
    if k == 1:
        return sign(sympy.pi)/2
    if k == 2:
        return sign(sympy.pi)/3
    if k == 3:
        return sign(sympy.pi)/4
    if k == 4:
        return sign(sympy.pi)/6

# pick a trig function between sin and cos
def trigSinCos(y):
    k = random.randrange(2)
    if k == 0:
        return sympy.sin(y)
    else:
        return sympy.cos(y)

# generate a sin or cos function with deformations
def trigFunc():  
    a = random.randrange(1,4)
    b = random.randrange(1,4)
    c = trigValue()

    # expression inside sin or cos
    ex = "y = " + sympy.latex(a * trigSinCos(b * x - c) + trigRoot())
    return ex
############################### END ###############################

############################### TOPIC 8: TRIGONOMETRIC EXPRESSIONS AND EQUATIONS ###############################

# trigonometric equation in normal(?) format
def basicTrigEq():
    eq = sympy.latex(trigSinCos(x)) + " = " + sympy.latex((trigRoot()))
    return eq

# generic trigonometric equation w multiple steps
def trigEq():
    a = random.randrange(1,4)
    b = random.randrange(1,4)
    c = trigValue()

    # expression inside sin or cos
    eq = sympy.latex(a * trigSinCos(b * x - c)) + " = " + sympy.latex(trigRoot() * a)
    return eq

# trigonometric equations to be solved by substitution (or sometimes factorization)
def trigSubs():
    # get two roots for quadratic equation
    a = trigRoot()
    b = trigRoot()

    # get the trig function

    eq = equify(sympy.latex(sympy.expand((x - a)*(x - b)).subs(x,trigSinCos(x))))
    return eq

# randomly pick a type of trig equation
def trigEqMix():
    k = random.randrange(3)
    if k == 0:
        return basicTrigEq()
    if k == 1:
        return trigSubs()
    if k ==2:
        return trigEq()
############################### END ###############################