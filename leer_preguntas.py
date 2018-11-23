import random
import sim

class Pregunta():
	literal = ""
	ecuacion = ""
	respuesta = "0"
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
				
			preguntas.append(pr)
		except Exception as ex:
			preguntas.append(pr)
			#print(ex)
	tmp=0
	for pr in preguntas:
		pr.respuestas=[]	
		pr.respuestas.append(pr.respuesta) #pongo la respuesta en cada pregunta
		lista_num_aleat=[]
		lista_num_aleat= list(range(1,9))
		
		
		while len(pr.respuestas)!=4:
			pr.respuestas=list(set(pr.respuestas))
			flag = False
			i=0
			while not flag:
				i= random.randint(1,len(pr.respuesta)-1)
				if pr.respuesta[i].isdigit():
					#print("DIG"+str( pr.respuesta[i]))
					dg=random.randint(1,10-int(pr.respuesta[i]))
					dig = int(pr.respuesta[i])+dg
					flag=True
			resp=pr.respuesta[0:i]+str(dig)+pr.respuesta[i+random.randint(0,1):]
			pr.respuestas.append(resp)
		
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
