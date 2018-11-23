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

	for pr in preguntas:
		pr.respuestas=[]	
		pr.respuestas.append(pr.respuesta) #pongo la respuesta en cada pregunta
		for i in range(0,3):#genero 3 respuestas (esocojo la respuesta y le sumo un aleatorio)
			pa=False
			while not pa:
				indice_primer_numero=-1
				esta_con_menos=False
				for i in range(0,len(pr.respuesta)):
					if pr.respuesta[i].isdigit():
						indice_primer_numero=i
						break
				try:#Escojo hasta que agarre un numero...
					fin = len(pr.respuesta)
					i = random.randint(0,fin)			
					if pr.respuesta[i].isdigit():
						digito=pr.respuesta[i]
						dig = int(digito)+random.randint(0,digito-1)
						if 1==random.randint(0,1) and i==indice_primer_numero and esta_con_menos:
							dig = -dig
							esta_con_menos=True
						resp=pr.respuesta[0:i]+str(dig)+pr.respuesta[i+1:]
						#print("Resp. "+pr.respuesta+" Random:"+resp)
						
						pr.respuestas.append(resp)

						pa = True
				except Exception as ex:
					#print("EOF"+str(ex))
					pass
		random.shuffle(pr.respuestas)
	random.shuffle(preguntas)
	return preguntas
