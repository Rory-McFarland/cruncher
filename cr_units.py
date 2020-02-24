"""
cr_units
Cruncher Units Module
    Module for defining common units in Cruncher

    By Rory McFarland, Dr. Darci Snowden
    Developed at Central Washington University

    9 July 2019
    Rev 1.0.0, compiled 9 July 2019
"""
# modules
from decimal import *
from copy import *

# unit definition
class unit:
    def __init__(self, dimension: str, basis: str, offset=None):
        self.dimension = dimension
        self.basis = Decimal(basis)
        # offset is used for units fixed to a linear scale. The following formula is used
        # quantity in standard unit = basis*x + offset where x is the quantity in the given unit
        # units not fixed to a scale do not need to specify an offset
        if offset is None:
            self.offset = Decimal('0')
        else:
            self.offset = Decimal(offset)


# prefixes
prefix = {
    'y': -24,
    'z': -21,
    'a': -18,
    'f': -15,
    'p': -12,
    'n': -9,
    'u': -6,
    'm': -3,
    'c': -2,
    'd': -1,
    '': 0,
    'da': 1,
    'h': 2,
    'k': 3,
    'M': 6,
    'G': 9,
    'T': 12,
    'P': 15,
    'E': 18,
    'Z': 21,
    'Y': 24,
}
# dimensions
dimensions = ['L', 'M', 'T', 'O', 'I']
compositedimensions = ['[PPO2]', '[PPN2]', '[PPF2]']
# ==============
# built-in units
# ==============

# BASE UNITS

# Null unit
null = unit('_', '1.000000000')
# Distance units
# standard unit
meter = unit('L', '1.00000000')
# imperial
inch = unit('L', '2.54E-2')
foot = unit('L', '3.048E-1')
yard = unit('L', '9.144E-1')
mile = unit('L', '1.609344E3')
nmile = unit('L', '1.852E3')
league = unit('L', '5.556E3')  # using definition 1 league = 3 nautical mile

# Mass unit
# standard unit
gram = unit('M', '1.00000000')
# imperial
grain = unit('M', '6.479891E-2')
drachm = unit('M', '1.77184520')
ounce = unit('M', '2.834952E1')  # avoirdupois ounce
tounce = unit('M', '3.110348E1')  # troy ounce
pound = unit('M', '4.45359237E2')  # avoirdupois pound
stone = unit('M', '6.35029318E3')
ston = unit('M', '9.0718474E5')  # also refered to as "ton" in the US
lton = unit('M', '1.0160469088E6')
mton = unit('M', '1.00000000E6')  # also a megagram

# Time unit
# standard unit
second = unit('T', '1.00000000')
# traditional units
minute = unit('T', '6.00000000E1')
hour = unit('T', '3.60000000E3')
day = unit('T', '8.64000000E4')  # Civil day. Exact day not included due to variance.
week = unit('T', '6.04800000E5')  # Civil week. Exact week not included due to variance.
fortnite = unit('T', '1.2096E6')
amonth = unit('T', '2.6298E6')  # Average number of days in a month
year = unit('T', '3.155695E7')  # Using a Gregorian Calandar
cyear = unit('T', '3.1536E7')  # Common year, 365 days
lyear = unit('T', '3.16224E7')  # Leap year, 366 days

# atomic and molecular units
timeplank = unit('T', '5.39124560E-44')
jiffy = unit('T', '3E-24')  # Note: Multiple definitions exist
svedberg = unit('T', '1.000000000E-13')
# engineering units
TU = unit('T', '1.024E-3')

# Temperature units !DONE!
# standard unit
kelvin = unit('O', '1.00000000')
# common units
celsius = unit('O', '1.00000000', '273.15')
fahrenheit = unit('O', '0.55555555', '255.37')
rankine = unit('O', '0.55555555')
# antiquated units
delisle = unit('O', '-0.66666666', '373.15')
tnewton = unit('O', '3.03030303', '273.15')
reaumur = unit('O', '1.25000000', '273.15')
romer = unit('O', '1.90476190', '258.864286')
# atomic units
tempplank = unit('O', '1.417E32')

# Charge units !DONE!
# standard unit
coulomb = unit('I', '1.00000000')
# common units
faraday = unit('I', '9.64853329E4')
# atomic units
elemc = unit('I', '1.60217663E-19')


#list of all units (used for search purposes)
unitindex = [null, meter, inch, foot, yard, mile, nmile, league, gram, grain, drachm, ounce, tounce, pound, ston, ston, lton, mton, second, minute, hour, day, week, fortnite, amonth, year, cyear, lyear, timeplank, jiffy, svedberg, TU, kelvin, celsius, fahrenheit, rankine, tnewton, reaumur, romer, tempplank, coulomb, faraday, elemc]
# ====================
# FUNCTION DEFINITIONS
# ====================

def dimreduce(u: unit) -> str:
    dim = u.dimension
    # remove '_' dimensions
    dim.replace('_', '')

    for c in sorted(dimensions):
        # determine number of positive and negative power dimensions are present
        diff = dim.count(c.upper()) - dim.count(c.lower())
        # remove existing dimension
        dim = dim.replace(c.upper(), '')
        dim = dim.replace(c.lower(), '')
        # add appropriate degree of dimension
        if diff > 0:
            for i in range(0, diff):
                dim += c.upper()
        if diff < 0:
            for i in range(0, -1 * diff):
                dim += c.lower()

    # give blank dimension if no dimension is present
    if dim == '':
        dim = '_'
    # return
    return dim


def compdimreduce(u: unit) -> str:
    dim = u.dimension
    # remove '_' dimensions
    dim.replace('_', '')

    for c in sorted(compositedimensions):
        # determine number of positive and negative power dimensions are present
        diff = dim.count(c.upper()) - dim.count(c.lower())
        # remove existing dimension
        dim = dim.replace(c.upper(), '')
        dim = dim.replace(c.lower(), '')
        # add appropriate degree of dimension
        if diff > 0:
            for i in range(0, diff):
                dim += c.upper()
        if diff < 0:
            for i in range(0, -1 * diff):
                dim += c.lower()

    # give blank dimension if no dimension is present
    if dim == '':
        dim = '_'
    # return
    return dim


def fulldimreduce(u: unit) -> str:
    dim = compdimreduce(u)
    # find and remove compound section
    comp = dim[dim.find('[', 0, len(dim) + 1):dim.rfind(']', 0, len(dim)) + 1]
    dim = dim.replace(comp, '')
    # reduce physical section
    for c in sorted(dimensions):
        # determine number of positive and negative power dimensions are present
        diff = dim.count(c.upper()) - dim.count(c.lower())
        # remove existing dimension
        dim = dim.replace(c.upper(), '')
        dim = dim.replace(c.lower(), '')
        # add appropriate degree of dimension
        if diff > 0:
            for i in range(0, diff):
                dim += c.upper()
        if diff < 0:
            for i in range(0, -1 * diff):
                dim += c.lower()
    # reintroduce compound section
    dim += comp
    # remove '_' dimensions
    dim.replace('_', '')
    # give blank dimension if no dimension is present
    if (dim == ''):
        dim = '_'
    return dim


# Convert value from originalunit to outputunit
def convert(value, originalunit, outputunit):
    originalunit: unit
    outputunit: unit

    if(originalunit != outputunit):
        return Decimal(value) * outputunit.basis / originalunit.basis
    else:
        return value

def combine(u1: unit, u2: unit, flag: int):
    #soft typing
    u1: unit
    u2: unit
    u3: unit
    flag: int
    #define return product
    u3 = copy(unit('', '1.00000000'))
    #multiply
    if(flag == 1):
        u3.basis = u1.basis * u2.basis
        u3.dimension = u1.dimension + u2.dimension
        u3.dimension = fulldimreduce(u3)
    #divide
    if (flag == -1):
        u3.basis = u1.basis / u2.basis
        u3.dimension = u1.dimension + u2.dimension.swapcase()
        u3.dimension = fulldimreduce(u3)

    return u3
# return defined unit from constructed unit
    # NOTE: This funcion ensures that identical units all reside at the same memory address, thus avoiding problems with unit redefinitions
def search (dim: str, bas: Decimal):
    bas = Decimal(bas)
    dim = fulldimreduce(unit(dim, bas))
    matchingunit = null
    for u in unitindex:
        if(u.basis == bas and u.dimension == dim):
            matchingunit = u
            break
    return matchingunit

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