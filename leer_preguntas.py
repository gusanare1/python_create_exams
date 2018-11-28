import random
import sim
import sympy
import time
import mpmath
from mpmath import radians,degrees
class Pregunta():
	literal = ""
	ecuacion = ""
	respuesta = "0"
	#----exec(string)
	exe=""
	dato=""#numero a cambiar
	respuestas=[]
	def __str__(self):
		retorno = ""
		if self.literal:
			retorno = retorno+"Literal: "+self.literal
		if self.ecuacion:
			retorno = retorno+" *Ecuacion: "+self.ecuacion
		if self.respuesta:
			retorno = retorno+" *Respuesta: "+self.respuesta
			retorno = retorno+str(self.respuestas)
		if self.exe:
			retorno=retorno+" *Exec:"+str(self.exe)
		if self.dato:
			retorno=retorno+" *Dato:"+str(self.dato)
		
		return retorno


    
def crear_preguntas():
	preguntas = []	
	with open('preguntas.txt') as f:
		lines_t = f.readlines()

	lines = []
	for line in reversed(lines_t):
		if  line.strip():
			lines.append(line)
	while lines:
		try:
			pr = Pregunta()
			pr.literal=lines.pop().replace("P:","").replace("\n","")
			while not 'P:' in lines[len(lines)-1]:
				if 'E:' in lines[len(lines)-1]:
					pr.ecuacion = lines.pop().replace("E:","").replace("\n","")
				if 'R:' in lines[len(lines)-1]:
					pr.respuesta = lines.pop().replace("R:","").replace("\n","")
				if 'DD:' in lines[len(lines)-1]:
					pr.dato = lines.pop().replace("DD:","").replace("\n","")
				if 'Z:' in lines[len(lines)-1]:
					pr.exe = lines.pop().replace("Z:","").replace("\n","")
			
			pr.literal=pr.literal.replace("XX",pr.dato)
			pr.exe=pr.exe.replace("XX",pr.dato)
			preguntas.append(pr)
		except Exception as ex:
			preguntas.append(pr)
			#print(ex)
	
	for pr in preguntas:
		#print("Entramos a preguntas")
		pr.respuestas=[]
		if pr.exe:
			al="tmp="+pr.exe+""
			#print("*****"+al)
			exec(al, globals())			
			#print(tmp)
			tmp2="%4.2f" % (tmp)
			pr.respuesta=pr.respuesta.replace("YY",str(tmp2))
			#print(pr.respuesta)
		#print(pr)
		pr.respuestas.append(pr.respuesta) #pongo la respuesta en cada pregunta
		
		while len(pr.respuestas)!=4:
			flag = False
			i=0
			while not flag:
				i= random.randint(1,len(pr.respuesta)-1)
				if pr.respuesta[i].isdigit():
					#print("DIG"+str( pr.respuesta[i]))
					dig=random.randint(5,50)
					if 0==random.randint(0,1):
						if "-" in pr.respuesta:
							pr.respuesta.replace("-","+")
						elif "+" in pr.respuesta:
							pr.respuesta.replace("+","-")
					while dig>9:
						dig=int(str(dig)[0])+int(str(dig)[1])
					
					flag=True
			resp=pr.respuesta[0:i]+str(dig)+pr.respuesta[i+1:]
			pr.respuestas.append(resp)
			pr.respuestas=list(set(pr.respuestas))
		'''
		for j in range(0,3):#genero 3 respuestas (esocojo la respuesta y le sumo un aleatorio)
			pa=False
			
			indice_primer_numero=-1
			for k in range(0,len(pr.respuesta)):
					if pr.respuesta[k].isdigit():
						indice_primer_numero=k
						break
			while not pa:
				
				try:#Escojo hasta que agarre un numero...
					
					fin = len(pr.respuesta)
					i = random.randint(0,fin)			
					if pr.respuesta[i].isdigit():
						digito=int(pr.respuesta[i])
						
						
						
						sol = 10
						while sol<9:
							t=random.choice(lista_num_aleat)
							lista_num_aleat.remove(t)
							if sol+t<10:
								sol=sol+t
						
						dig=sol
						if 1==random.randint(0,1) and not i==indice_primer_numero:
							if "+" in pr.respuesta[0:i]:
								pr.respuesta[0:i].replace("+","-")
						if 1==random.randint(0,1):
							if "-" in pr.respuesta[i:]:
								pr.respuesta[i:].replace("-","+")
						resp=pr.respuesta[0:i]+str(dig)+pr.respuesta[i+random.randint(0,1):]
						#print("Resp. "+pr.respuesta+" Random:"+resp)
						print(" "+str(pr.respuesta))
						pr.respuestas.append(resp)

						pa = True #Si llego hasta aqui he cambiado un numero
				except Exception as ex:
					#print("EOF"+str(ex))
					pass
		'''
		random.shuffle(pr.respuestas)
		
	random.shuffle(preguntas)
	return preguntas
