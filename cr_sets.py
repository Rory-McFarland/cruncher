"""
cr_sets
Cruncher Sets Module
    Module for defining sets in Cruncher

    By Rory McFarland, Dr. Darci Snowden
    Developed at Central Washington University

    29 July 2019
    Rev 1.0.0, compiled 9 July 2019
"""
# built-in imports
import math
# cr imports
import cr_units as units
import cr_elements as elm
#
from decimal import *

# set definitions
# psets and nsets will be developed at a later time
"""class pset:
    def __init__(self, dimension, data):
        self.dimension = dimension
        self.data = pimport(data)
"""


class set:
    def __init__(self, data=[], unit=units.null, sigfigs=(0, 0), stats=False):
        # soft typing
        data: list[object]
        unit: unit
        sigfigs: tuple[int]
        stats: stats

        #assign values
        self.data = data
        self.unit = unit
        # convert units
        self.data = homogenizeunits(data, unit)
        # determine set sig figs
        if (sigfigs == (0, 0)):

            lowestsigfig = self.data[0].sigfigs[1]
            #find lowest sig fig in set
            for i in range(len(data)):
                if (data[i].sigfigs[1] < lowestsigfig):
                    lowestsigfig = data[i].sigfigs[1]
            # take lowest sig figs
            self.sigfigs = (1, lowestsigfig)

            #set properties
            self.length = len(data)

class stats:

    def __init__(self, data):
        # calculate mean
        for e in data:
            self.mean += e.value * 10**Decimal(e.magnitude)
        self.mean = self.mean/data.length

        #calculate variance and standard deviation

# ====================
# FUNCTION DEFINITIONS
# ====================

# Make units consistant within set
def homogenizeunits(data, unit):
    e: elm.el
    for e in data:
        e.value = units.convert(e.value, e.unit, unit)
    return data


def determinesigfigs(data):
    e: elm.el
    sigfigs = 0
    for e in data:
        if e.value > sigfigs:
            sigfigs = e.value
    return int(sigfigs)


def dataimport(data):
    imp = []
    for d in data:
        try:
            value = Decimal(d)
            if (not value.is_nan()):
                imp.append(elm.el(d))
        except:
            print(d + ' is not a number')


def easyset(data, unit):
    for i in range(len(data)):
        data[i] = elm.el(data[i], unit)
    return set(data, unit)


def add(s1, s2, flag = 1):
    # soft typing
    s1: set
    s2: set
    flag: int

    #test length
    if (len(s1.data) == len(s2.data)):
        #perform operation
        indata = []
        for i in range(len(s1.data)):
            indata.append(elm.add(s1.data[i], s2.data[i], flag))
        # generate product set
        s3 = set(indata, s1.unit)
        return s3

def multiply(s1, s2, flag):
    # soft typing
    s1: set
    s2: set
    flag: int

    #test length
    if (len(s1.data) == len(s2.data)):
        #perform operation
        indata = []
        for i in range(len(s1.data)):
            indata.append(elm.multiply(s1.data[i], s2.data[i], flag))
        # generate product set
        s3 = set(indata, units.combine(s1.unit, s2.unit, flag))
        return s3

def readout(s):
    #soft typing
    s: set

    #read out set information
    print('This set contains ' + str(s.length) + ' elements')
    print('The elements in the set have a unit of ' + s.unit.dimension)
    print('This set has a significance of ' + str(s.sigfigs[0] + s.sigfigs[1]))
    print('The data is as follows:')
    for i in range(s.length):
        print(str(s.data[i].value))
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