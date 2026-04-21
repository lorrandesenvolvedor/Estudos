# oque são tuplas? tuplas são variáveis que contém várias variáveis, elas não tem um nome necessário, podemos adicionar qualquer nome para elas

#exemplo:

tuplas = (25, 29, "Lorran")

#executando 

print(tuplas[0])
#nesse exemplo acima, está imprimindo um dos resultados da variável, aí no caso o 0 significa o primeiro elemento da lista que no caso e 25, caso queríamos imprimir resultado 29 podemos colocar [1] porque no python começamos do zero.

#________________________________________________
# segundo exemplo;

índice = 0
while índice < len (tuplas):
     print(tuplas[índice])
     índice = índice + 1
     #acabamos de fazer um exemplo que pega o conteúdo de tuplas, e logo após imprime cada conteúdo que ali dentro está.
     


#______________________________________________

# variáveis com tuplas.

nome = input("digite o seu nome") 

idade = int(input("digite a sua idade"))  

tuplas = (nome, idade)

índice = 0
while índice < len (tuplas):
     print(tuplas[índice])
     índice = índice + 1       
# como podemos observar , não mudou nada, somente trocamos os valores de tuplas pelas variáveis .   