"""
cr_elements
Cruncher Units Module
    Module for defining elements in Cruncher

    By Rory McFarland, Dr. Darci Snowden
    Developed at Central Washington University

    21 July 2019
    Rev 1.0.0, compiled 21 July 2019
"""

# cr imports
import cr_units as units

# built-in imports
from decimal import *
import enum
import math


# Element types
class eltype(enum.IntEnum):
    # numeric
    DECIMAL = 1
    BINARY = 2
    OCTAL = 3
    HEXADECIMAL = 4
    # complex
    COMPLEX = 5
    # logic
    BOOLEAN = 6
    # Other
    STRING = 7
    DATETIME = 8
    OTHER = 9


# Element class
# Used for all elements (of a set or data set)
class el:
    def __init__(self, value: str = '0', unit: object = units.null, ty: int = eltype.DECIMAL,
                 prefix: int = units.prefix[''],
                 sigfigs: tuple = (0, 0), error: str = '0'):

        # For decimals (currently only type supported)
        if (ty == eltype.DECIMAL):

            # soft typing
            self.value: Decimal
            self.magnitude: int
            self.unit: units.unit
            self.prefix: int
            self.sigfigs: tuple
            self.error: Decimal
            self.ty: int

            # Assign values
            self.value = Decimal(value)
            # order of magnitude of the value
            self.magnitude = self.value.adjusted() + prefix
            # Keep in scientific notation
            self.value = self.value * Decimal(10) ** (-self.magnitude)
            self.unit = unit
            # Determine sig figs if not specified
            if (sigfigs == (0, 0)):
                self.sigfigs = (1, abs(self.value.as_tuple().exponent))
            else:
                self.sigfigs = sigfigs
            # Assign other values
            self.error = Decimal(error)
            self.ty = eltype.DECIMAL

        if (ty == eltype.OTHER):
            self.value = value
            self.unit = unit
            self.ty = eltype.OTHER
            # Expand here

class con:
    def __init__(self, value: str = '0', unit: object = units.null, ty: int = eltype.DECIMAL,
                 prefix: int = units.prefix[''], error: str = '0'):

        # For decimals (currently only type supported)
        if (ty == eltype.DECIMAL):

            # soft typing
            self.value: Decimal
            self.magnitude: int
            self.unit: units.unit
            self.prefix: int
            self.sigfigs: str
            self.error: Decimal
            self.ty: int

            # Assign values
            self.value = Decimal(value)
            # order of magnitude of the value
            self.magnitude = self.value.adjusted() + prefix
            # Keep in scientific notation
            self.value = self.value * Decimal(10) ** (-self.magnitude)
            self.unit = unit
            # Determine sig figs if not specified
            self.sigfigs = 'C'
            # Assign other values
            self.error = Decimal(error)
            self.ty = eltype.DECIMAL

        if (ty == eltype.OTHER):
            self.value = value
            self.unit = unit
            self.ty = eltype.OTHER
# =========
# CONSTANTS
# =========
# Mathematical
pi = con('3.14159265', units.null, eltype.DECIMAL)
goldenratio = con('1.61803399', units.null, eltype.DECIMAL)
e = con('2.71828183', units.null, eltype.DECIMAL)
# Physical

# Internal
pgmerror = el('ERROR', units.null, eltype.OTHER)


# =========
# FUNCTIONS
# =========
# ============
# Interactions
# ============
class opflag(enum.IntEnum):
    SUM = 1
    PRODUCT = 2
    POWER = 3
    EXP = 4
    LOG = 5
    TRIG = 6


def sigfigshift(s: tuple):
    if (s[0] != 1):
        s = (1, s[1] + (s[0] - 1))
    return s


def sigfigreduce(e1, e2, flag):
    # soft typing
    e1: el
    e2: el
    flag: int

    #constant exception
    if(e1.sigfigs == 'C'):
        return sigfigshift(e2.sigfigs)
    if (e2.sigfigs == 'C'):
        return sigfigshift(e1.sigfigs)

    # Shift sigfigs to (1, f) form
    e1.sigfigs = sigfigshift(e1.sigfigs)
    e2.sigfigs = sigfigshift(e2.sigfigs)

    if (flag == opflag.SUM or flag == opflag.PRODUCT or flag == opflag.POWER):
        # Return lowest fractional significance
        f3 = min([e1.sigfigs[1], e2.sigfigs[1]])
        return (1, f3)


def dimensionalcheck(e1: el, e2: el):
    return units.fulldimreduce(e1.unit) == units.fulldimreduce(e2.unit)

    # ============
    # Mathematical
    # ============


def add(e1, e2, flag = 1):
    #Returns Y in the case of Y = x1 + x2
    # soft typing
    e1: el
    e2: el
    flag: int

    # check dimensional compatability
    if (not dimensionalcheck(e1, e2)):
        # error handle
        return pgmerror

    # define sum element
    e3 = el()
    # perform additions
    e2.value = units.convert(e2.value, e2.unit, e1.unit)  # convert units of e2 to that of e1
    e3.value = e1.value + e2.value * flag  # add/subtract
    e3.magnitude = max([e1.magnitude, e2.magnitude])  # determine magnitude
    # correct magnitude if necessary
    if (e3.value >= Decimal('10')):
        e3.value = e3.value * Decimal('10') ** (-1)  # return to scientific notation
        e3.magnitude += 1  # adjust magnitude

    if (e3.value < Decimal('1') and e3.value > Decimal('0')):
        e3.value = e3.value * Decimal('10') ** (1)  # return to scientific notation
        e3.magnitude -= 1  # adjust magnitude
    # define unit
    e3.unit = e1.unit

    # define sig figs
    e3.sigfigs = sigfigreduce(e1, e2, flag)
    # propagate error
    e3.error = Decimal(math.sqrt((e1.error * 10 ** (e1.magnitude)) ** 2 + (e2.error* 10 ** (e1.magnitude)) ** 2))

    return e3


def multiply(e1, e2, flag = 1):
    #Returns Y in the case of Y = x1 * x2.

    # soft typing
    e1: el
    e2: el
    flag: int

    # define product element
    e3 = el()
    # perform operation
    e2.value = units.convert(e2.value, e2.unit, e1.unit)  # convert units of e2 to that of e1
    if (flag == 1):
        e3.value = e1.value * e2.value  # multiply
    if(flag == -1):
        e3.value = e1.value / e2.value  # divide

    e3.magnitude = e1.magnitude + e2.magnitude  # determine magnitude
    # correct magnitude if necessary
    if (e3.value >= Decimal('10')):
        e3.value = e3.value * Decimal('10') ** (-1)  # return to scientific notation
        e3.magnitude += 1  # adjust magnitude
    if (e3.value < Decimal('1')):
        e3.value = e3.value * Decimal('10') ** (1)  # return to scientific notation
        e3.magnitude -= 1  # adjust magnitude

    # define unit
    e3.unit = units.combine(e1.unit, e2.unit, flag)
    #match to existing unit
    trymatch = units.search(e3.unit.dimension, e3.unit.basis)

    if(trymatch != units.null):
        e3.unit = trymatch
    # define sig figs
    e3.sigfigs = sigfigreduce(e1, e2, flag)

    # propogate error
    e3.error = Decimal(e3.value * Decimal(math.sqrt((e1.error / e1.value * 10**(e1.magnitude)) ** 2 + (e2.error / e2.value * 10**(e1.magnitude)) ** 2)))

    return e3

def power(e1, n):
    #Returns Y in the case of Y = x^n. n must be an exact value (i.e. error of n = 0). n must be dimensionless

    #soft typing
    e1: el

    #extract n
    if(type(n) == el):
        if(units.fulldimreduce(n.unit.dimension) == '_'):
            n = n.value
        else:
            n = pgmerror
    #define power element
    e3 = el()
    #perform operation
    e3.value = e1.value**n.value
    #Determine significant figures
    e3.sigfigs=sigfigreduce(e1,e1,1)
    # propogate error
    if(n == -1): #special case
        e3.error = Decimal((e1.error/e1.value)*e3.value)
    else:
        e3.error = Decimal(abs(n) * e1.value**(n-1) * e1.error)

def exponent(e1, b = e):
    # Returns Y in the case of Y = b^x. b must be an exact number. x must be dimensionless.
    #soft typing
    e1: el
    #b: con or el
    #define exponent element
    e3 = el()

    # determine if x is dimensionless, if so perform operation
    if(e1.unit.dimension == '_'):
        e3.value = b.value**e1.value
    else:
        e3 = pgmerror
    # determine sigfigs
    if (e1.sigfigs(2) == 0):  # Special case
        e3.sigfigs = (1, 0)
    else:
        e3.sigfigs = (1, e1.sigfigs(1) - 1)
    return e3

def parseinput(inp:str):
    # remove spaces
    inp = inp.replace(' ', '')
    # remove commas (for incorectly formated numberes)
    inp = inp.replace(' ','')
    # get value string
    val = []
    for c in inp:
        if c.isnumeric() or c == '.':
            val.append(c)
    val = str(val)
    # reslice string
    inp = inp[len(val)-1:]
    # correct order of magnitude
    if inp[0].upper() == 'E' and (inp[1] == '+' or inp[1] == '-' or inp[1].isnumeric()):
        inp = inp[1:]
        exp = []
        for c in inp:
            if c.isnumeric() or c == '+' or c == '-':
                exp.append(c)
        val = val + 'E' + exp


# Copyright notice
"""
Copyright 2019 Rory McFarland

This file is part of Cruncher.

Cruncher is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Cruncher is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Cruncher. If not, see <https://www.gnu.org/licenses/>.
"""