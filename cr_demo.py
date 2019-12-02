# Import cr_data modules
import cr_units as units
import cr_elements as elm
import cr_sets as sets

# Demo 1: Units and unit conversion
"""
#show the elements of a unit
print("This is the basis and dimension of a meter")
print(units.meter.basis, units.meter.dimension)
#convert 1 meter to feet
print("Converting 1 foot to 1 meter [basis, dimension]")
print(units.convert('1', units.foot, units.meter), units.foot.dimension)
#combining units
print("Comining 1 m and 1/s [basis, dimension]")
print(units.combine(units.meter, units.second, -1).basis, units.combine(units.meter, units.second, -1).dimension)
"""

# Demo 2: Element operations
"""
#define 3 elements
e1 = elm.el('1.23', units.foot, elm.eltype.DECIMAL, units.prefix['k'],(0,0), '0.02')
e2 = elm.el('9.87', units.foot, elm.eltype.DECIMAL, units.prefix['n'],(0,0), '0.07')
e3 = elm.el('3.14', units.gram, elm.eltype.DECIMAL, units.prefix['d'], (0,0), '1.1')
#perform addition, subtraction, multiplication
ea = elm.add(e1, e2, 1)
es = elm.add(e1, e2, -1)
em = elm.multiply(e1, e3, 1)
#return values
print("value|sig figs|error|dimension")
print('ea')
print(ea.value*10**ea.magnitude, '|', ea.sigfigs,'|',  ea.error, '|', ea.unit.dimension)
print('es')
print(es.value*10**es.magnitude,'|' , es.sigfigs,'|',  es.error, '|', es.unit.dimension)
print('em')
print(em.value*10**em.magnitude,'|', em.sigfigs,'|', em.error, '|', em.unit.dimension)
"""
# Demo 3: Set operations
"""
#define 3 sets
s1 = sets.easyset(['1.1','2.2','3.3','4.4','5.5'], units.coulomb)
s2 = sets.easyset(['-1.1','-2.2','-3.3','-4.4','-5.5'], units.coulomb)
s3 = sets.easyset(['99','88','77','66','55'], units.meter)

#perform addition and multiplication
sa = sets.add(s1, s2, 1)
sm = sets.multiply(s1, s3, 1)
#return values
print('sa')
sets.readout(sa)
print('sm')
sets.readout(sm)
"""