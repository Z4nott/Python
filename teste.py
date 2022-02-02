# -*- coding: utf-8 -*- Para aceitar caracteres especiais precisa colocar esse comando.
# comentario do comentario que foi feito de um comentario

print("Aopa!")

print(10*3) 
print(4/2)
print(1+1)
print(10%3)


# criando variavel no Python

minha_variavel = "Teste"
print("Teste")
print("Teste")

var1 = 1 # variavel inteira
var2 = 1.1 # variavel float
var3 = "String"	# variavel
var4 = ("true") # verdadeiro

print(var1)
print(var2)
print(var3)
print(var4)

# operadores

x = 3
y = 1
z = 3

soma = x + y

print(x == y and x == z)

# comando else

x = 10 
y = 2

if x > y:
	print("x maior que y")
else:
	print("x não é maior que y")	

# comando elif

x = 2
y = 2 

if x == y:
	print("numeros iguais")
elif x < y:
	print("x menor que y")
elif y > x:
	print("y maior qie x")
else:
	print("numeros diferentes")			

# comando WHILE "comando de repetição"

x = 1

while x < 3:
	print(x)
	x += 1 #isso seria tipo x = x + 1


# comando FOR "para"

lista1 = [1,2,3,4,5]
lista2 = ["Olá", "Mundo", "!"]
lista3 = [0,"Olá","Bolacha","Suco",9.99]

for i in lista3:
	print(i)

# estrutura de repetição (comando FOR e RANGE)

for i in range(10,20,2):
	print(i)

# exemplo de STINGS

a = "Augusto"
b = "Cesar"

concatenar = a + " " + b
print(concatenar)
tamanho = len(concatenar)
print(tamanho)


#Funções

def soma(x, y):
	return x+y

def multiplicacao(x, y):
	return x*y

s = soma(2, 3)
m = multiplicacao(1, 4)

print(soma(s, m,))

# Lista

minha_lista = ["abacate", "melancia", "abacate"]
minha_lista_2 = [1,2,3,4,5]	
minha_lista_3 = ["abacaxi", 2, 9.89, True]

minha_lista_4 = [] #---> lista em branco 

minha_lista_4.append(57)
print(minha_lista_2) # mudar a lista para imprimir 

lista = [123, 751, 2, 67, 11, 32, 10]

lista.sort(reverse=False) #"reverse" para inverter a ordem / "true" deixa do maior para o menor e "false" deixa na ordem crescente
print(lista)

# Dicionario
meu_dicionario = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}

for i in meu_dicionario.keys():
	#print(chave+"-"+meu_dicionario[chave])
	print(i)

# numeros aleatorios

import random

numero = random.randint(0,100)
print(numero)	




"""




"""













""" 
Operadores Logicos
 Operador AND Duas condiçôes sejam verdadeiras
 Operador OR pelo menos uma condição seja verdadeira
 Operador NOT inverte o valor
 


"""
# Comando usado para criar estruturas condicionais "IF"
