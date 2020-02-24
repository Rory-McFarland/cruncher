"""
cr_func
Cruncher Functions Module
    Module for defining numeric functions in Cruncher

    By Rory McFarland, Dr. Darci Snowden
    Developed at Central Washington University

    22 Feb 2020
    Rev 1.0.0, compiled 22 Feb 2020
"""
#Imports
import cr_units as units
import cr_elements as elm
import cr_sets as sets

# ----------------------
# DIFFERENTIAL EQUATIONS
# ----------------------
# Euler's Method
    # This is the most basic method for solving differential equations and is most commonly used as a pediological tool
def eulers_method (x, dx, h):

    # soft typing
    x: object
    dx: object
    h: object

    # test length
    if (len(dx.data) == len(h.data)) or (len(h.data) == 1 ):
        # Euler's method
        delx = sets.multiply(dx, h)
        y = [x]

        for i in range(len(delx.data)):
            y.append(elm.add(y[i], delx.data[i]))

        s3 = sets.set(y)
    return s3

def linear_regression(x, y):

    # Soft typing
    x: object
    y: object

