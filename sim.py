from pytexit import py2tex
from sympy import *
import sympy
from sympy import sympify
from sympy.solvers.solvers import solve_linear
from sympy.parsing.sympy_parser import parse_expr

import matplotlib.mathtext as mathtext
import matplotlib.pyplot as plt
import sympy

from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations,
    implicit_multiplication_application
)

def my_parse(s, transfm=None):
    lhs, rhs = s.split('=')
    if transfm is None:
        transfm = (standard_transformations +
            (implicit_multiplication_application,))
    return sympy.Eq(
        parse_expr(lhs, transformations=transfm),
        parse_expr(rhs, transformations=transfm))


from collections import defaultdict		
class GenerateSymbols(defaultdict):
    def __missing__(self, key):
        self[key] = sympy.Symbol(key)
        return self[key]
		
def ecuacion_to_jpg(eq, name_file):
	#eq = 'x+y=4'
	if '=' in eq:
		
		lf,rg = eq.split("=")
		eq=sympy.Eq(sympify(lf,evaluate=False),sympify(rg))
		
	formula_as_file(sympy.latex( eq ), name_file+'.png')

'''crear foto de la ecuacion'''	
def crear_foto(eq,nombre,tam=120):
	
		#add text                                                      
		plt.clf()                 
		plt.text(0, 0.5, r"$%s$" % eq, fontsize = tam)                                  

		#hide axes                                                                      
		fig = plt.gca()
		fig.axes.get_xaxis().set_visible(False)
		fig.axes.get_yaxis().set_visible(False)  
		plt.savefig(nombre) #or savefig                                                          

def ecuacion_to_latex(eq):
	if '=' in eq:
		
		lf,rg = eq.split("=")
		eq=sympy.Eq(sympify(lf,evaluate=False),sympify(rg))
		
	return sympy.latex(sympify(eq,evaluate=False))

import os, requests
 
def formula_as_file( formula, file):
    formula = formula.replace('\n', ' ')
    r = requests.get( 'http://latex.codecogs.com/png.latex?\dpi{{300}} {formula}'.format(formula=formula))
    print('http://latex.codecogs.com/gif.latex?%5Cdpi%7B300%7D%20%5Cbegin%7Bbmatrix%7D%202%20%26%200%20%5C%5C%200%20%26%202%20%5C%5C%20%5Cend%7Bbmatrix%7D')
    print(r.url)
    f = open(file, 'wb')
    f.write(r.content)
    f.close()
    
   

'''
import matplotlib.pyplot as plt                                                 
import sympy                                                                    

x = sympy.symbols('x')
#y = 1 + sympy.sin(sympy.sqrt(x**2 + 20))                                         
lat = sympy.latex(fr)

#add text                                                                       
plt.text(0, 0.6, r"$%s$" % lat, fontsize = 50)                                  

#hide axes                                                                      
fig = plt.gca()                                                                 
fig.axes.get_xaxis().set_visible(False)                                         
fig.axes.get_yaxis().set_visible(False)                                         
plt.draw() #or savefig                                                          
plt.show()
'''
