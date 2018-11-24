#https://sourceforge.net/projects/pywin32/
#con win32com
import doc1
import os
import subprocess
from win32com import client
import time
from tkinter import *
import random
import fileinput
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
def printWordDocument(filename):
		word = client.Dispatch("Word.Application")
		word.Documents.Open(filename)
		word.ActiveDocument.PrintOut()
		time.sleep(2)
		word.ActiveDocument.Close()
		word.Quit()
		
def fetch():
	numero=int(ent.get())+1
	root.quit()
	time.sleep(1)
	#print('Input => "%s"' % ent.get())              # get text
	
		
	for i in range(1,int(numero)):
		doc1.crear_docx(i)
		archivo = dir_path+"\\exam"+str(i)+".docx" 
		print("*Imprimiendo "+archivo)
		
		for line in fileinput.input("preguntas.txt", inplace=1):
			if "DD:" in line:
				sE=line[:3]+str(int(line[3:])+random.randint(1,20))+"\n"
				line = line.replace(line,sE)
			sys.stdout.write(line)
		#printWordDocument(archivo)
		
class Quitter(Frame):                          # subclass our GUI
    def __init__(self, parent=None):           # constructor method
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT)
    def quit(self):
        Frame.quit(self)
	
root = Tk()
root.title("Cuantos examenes desea?")
root.geometry("500x200")
ent = Entry(root)
ent.insert(0, '')                   # set text
ent.pack(side=TOP, fill=X)                         # grow horiz
     
ent.focus()                                        # save a click
ent.bind('<Return>', (lambda event: fetch()))      # on enter key
btn = Button(root, text='Imprimir', command=fetch)    # and on button 
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()
