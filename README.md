# python_create_exams
Funcion que crea un examen en word con un template(txt) usando matlabplot docx y sympy

Instalar dependencias:
pip install -r requirements.txt
<br/>
\ntesteado con python3
<br/>
Uso:
P: Resuelva la siguiente fraccion:            <->Preguntas
<br/>
E: 1/(2/(3*x)) = y                            <-> Ecuaciones
<br/>
R: 1/2                                        <->Fracciones
<br/>
P: Hola
<br/>
R: Matriz 1,2,3;1,2,3;8,0,0;1,5,7             <->Matrices
<br/>
P: DOJO
<br/>
E: 1/2+x
<br/>
P: Quisiera una pizza con 
<br/>
E: 1/2*x+3*PI

Genera una pagina docx con "el encabezado", las preguntas y sus literales (posibles respuestas) aleatorialente. Tambien genera un codigo qr (Respuestas en el orden que aparecen en el documento+1).
