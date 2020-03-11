import sys
import os
from random import randint	
from tkinter import *


class App:
	def __init__(self, master=None):
		self.fontePadrao = ("Arial", "10")
		self.primeiroContainer = Frame(master)
		self.primeiroContainer["pady"] = 10
		self.primeiroContainer.pack()

		self.segundoContainer = Frame(master)
		self.segundoContainer["padx"] = 20
		self.segundoContainer.pack()

		self.terceiroContainer = Frame(master)
		self.terceiroContainer["padx"] = 20
		self.terceiroContainer.pack()

		self.quartoContainer = Frame(master)
		self.quartoContainer["padx"] = 20
		self.quartoContainer.pack()

		self.quintoContainer = Frame(master)
		self.quintoContainer["pady"] = 20
		self.quintoContainer.pack()

		self.titulo = Label(self.primeiroContainer, text="Dados necessários")
		self.titulo["font"] = ("Arial", "10", "bold")
		self.titulo.pack()

		self.DirLabel = Label(self.segundoContainer,text="Nome do diretório", font=self.fontePadrao)
		self.DirLabel.pack(side=LEFT)

		self.Dir = Entry(self.segundoContainer)
		self.Dir["width"] = 30
		self.Dir["font"] = self.fontePadrao
		self.Dir.pack(side=LEFT)

		self.QtdLabel = Label(self.terceiroContainer, text="Qtd. de perfis", font=self.fontePadrao)
		self.QtdLabel.pack(side=LEFT)

		self.Qtd = Entry(self.terceiroContainer)
		self.Qtd["width"] = 30
		self.Qtd["font"] = self.fontePadrao
		self.Qtd.pack(side=LEFT)

		self.InicioLabel = Label(self.quartoContainer,text="Inicio", font=self.fontePadrao)
		self.InicioLabel.pack(side=LEFT)

		self.Inicio = Entry(self.quartoContainer)
		self.Inicio["width"] = 30
		self.Inicio["font"] = self.fontePadrao
		self.Inicio.pack(side=LEFT)


		self.autenticar = Button(self.quintoContainer)
		self.autenticar["text"] = "Gerar dados"
		self.autenticar["font"] = ("Calibri", "8")
		self.autenticar["width"] = 12
		self.autenticar["command"] = self.GeraDados
		self.autenticar.pack()

		self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao)
		self.mensagem.pack()

		try:
			i = int(self.Inicio.get())

		except ValueError:
			#Handle the exception
			self.mensagem["text"] = "O valor da quantidade e inicio devem ser números inteiros"

	def GeraDados(self):
		Diretorio = './' + self.Dir.get() #nome do diretório a ser criado
		Quantidade = self.Qtd.get() #quantidade de perfis a serem gerados
		Inicio = int(self.Inicio.get()) #ID inicial
		maximo= int(Inicio) + int(Quantidade) #ID máximo
		provedor = ['@gmail.com', '@hotmail.com'] #provedores dos emails
		os.makedirs(Diretorio) #cria um diretório com o nome informado
		nomes = open ('./info/nomes.txt', 'r')
		nomes = nomes.readlines()
		cursos = open ('./info/cursos.txt', 'r')
		cursos = cursos.readlines()
		telefone = "\n"
		j=0
		for i in range(int(Quantidade)):
			IDatual = str(Inicio)
			matricula = IDatual + "\n"
			nomearquivo = IDatual + '.txt'
			dirarquivo= Diretorio + '/' + nomearquivo 
			arquivo = open (dirarquivo, 'w')
			qtdNomes = int(len(nomes))	#Quantidade de nomes na lista
			random = randint(1, qtdNomes )
			qtdCursos = int(len(cursos)) #Quantidade de Cursos
			randomCurso = randint(0, 5 ) #curso aleatório
			randomEmail = randint(0, 1)	
			nome = nomes[random].split("\n")
			tuplaemail = (nome[0], provedor[randomEmail])
			while j < 11:
				if j == 2:
					telefone+= " "
				numero = str(randint(0,9))
				telefone += numero
				j+=1
			email = "%s%s" %(tuplaemail[0], tuplaemail[1])

			arquivo.write(matricula)
			arquivo.write(nomes[random])
			arquivo.write(cursos[randomCurso])
			arquivo.write(email)
			arquivo.write(telefone)
			arquivo.close()	
			Inicio +=1


root = Tk()
App(root)
root.mainloop()