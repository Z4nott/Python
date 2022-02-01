# -*- coding: utf-8 -*- Para aceitar caracteres especiais precisa colocar esse comando.
# comentario do comentario que foi feito de um comentario

print("Aopa!")

print(10*3) 
print(4/2)
print(1+1)
print(10%3)


# Criando variavel no Python.
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


""" 
Operadores Logicos
 Operador AND Duas condiçôes sejam verdadeiras
 Operador OR pelo menos uma condição seja verdadeira
 Operador NOT inverte o valor
 


"""
# Comando usado para criar estruturas condicionais "IF"
