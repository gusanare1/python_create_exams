from pytexit import py2tex
from sympy import *
import sympy
from sympy import sympify
from sympy.solvers.solvers import solve_linear
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
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


'''Conversion de arreglo bidimensional np to latex formato string'''
def bmatrix(a):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)
		
		
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
def crear_foto(eq,nombre,tam=120,esMatriz=False):
	plt.clf() 
	if esMatriz:
		import pandas as pd
		# Add a table at the bottom of the axes
		fig, axs =plt.subplots()
		
		axs.xaxis.set_visible(False) 
		axs.yaxis.set_visible(False)
	 
		df = pd.DataFrame(eq)
		table = axs.table(cellText=df.values,loc='center',colWidths=[0.1] * eq.shape[1])
		table.set_fontsize(20)
		table.scale(1.5, 1.5)  # may help
		
		fig.tight_layout()
		plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
		plt.savefig(nombre,bbox_inches='tight',pad_inches=-1) #or savefig  
	else:
		#add text                                                      
		                
		plt.text(0, 0.5, r"$%s$" % eq, fontsize = tam)                                  

		#hide axes                                                                      
		fig = plt.gca()
		fig.axes.get_xaxis().set_visible(False)
		fig.axes.get_yaxis().set_visible(False)  
		
		plt.savefig(nombre,bbox_inches='tight') #or savefig                                                          

def ecuacion_to_latex(eq):

	if 'Matriz' in eq:
		#Si es una matrix, devolvemos como  matiz numpy
		a=eq.replace('Matriz','').replace(',',' ')
		
		matrix=np.matrix(a)
		'''
		#TO LATEX
		from tabulate import tabulate
		st_lat = tabulate(matrix, tablefmt="latex", floatfmt=".2f")
		print(st_lat)
		return st_lat
		'''
		
		return matrix
		
		

	elif '=' in eq:
		
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
