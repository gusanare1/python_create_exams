# python_create_exams
Funcion que crea un examen en word con un template(txt) usando matlabplot docx y sympy

Instalar dependencias:
<br/>
<big><b><i>pip install -r requirements.txt</i></b></big>
<br/>
Testeado con python3.6
<br/>
Uso:
<br/>
P: Resuelva la siguiente fraccion: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#09;&#09;<->Preguntas
<br/>
E: ECUACIONES EN LATEX    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                        <-> Ecuaciones
<br/>
R: \frac{1}{2}            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                            <->Fracciones
<br/>
P: Hola
<br/>
R: Matriz 1,2,3;1,2,3;8,0,0;1,5,7   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          <->Matrices
<br/>
P: DOJO
<br/>
E:nombre_archivo.extension
<br/>
P: Quisiera una pizza con 
<br/>
E: 1/2*x+3*PI

New:<br/>
P: Un arbol de XX m de alto proyecta una sombra de 60 m de largo. Encontrar el angulo de elevacion aproximado del sol en ese momento.<br/>
R: YY\degree<br/> 
DD:73<br/>
Z:degrees(sympy.atan(XX/6))<br/>
<b>XX se reemplaza por el numero en DD</b><br/>
<b>YY es la respuesta luego de pasar Z por simpy</b><br/>
Genera una pagina docx con "el encabezado", las preguntas y sus literales (posibles respuestas) aleatorialente. Tambien genera un codigo qr (Respuestas en el orden que aparecen en el documento+1).
<br/>
<b>Necesita win32com en windows </b>
