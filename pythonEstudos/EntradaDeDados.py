# DE INÍCIO UMA ENTRADA DE DADOS E QUANDO O USUÁRIO PODE DIIGTA O VALOR OU O NOME SEM QUE ELE A ESTEJA ESCRITO. EX ABAIXO NO CÓD;

#aqui usamos a logica aonde iremos digitar.
nome = input ("digite seu nome")

#aqui e ainde vai nos amostrar (printar) o resultado
print (nome)

#______________________________________________

#OUTRA FORMA PODEMOS FAZER ELE ADICIONAR ALGO AMAIS COMO UMA SOMA, DA SEGUINTE FORMA:

#variavel
salario = input ("porfavor digite o quanto recebe")
adicional = input ("digite o adicional")

#logica que ira juntar o resultado das duas variáveis fazendo uma soma só. 
saldo = salario + adicional 

#ja aqui vemos que, ja que criamos a variavel saldo que ja vai somar o valor de salario e adicional, então puxamos somente a variável saldo. pois ela já tera o valor completo!
print (saldo)

#______________________________________________

#DE OUTRO MODO! O CÓD ACIMA VAI SOMENTE RESPONDE O RESULTADO JUNTO SEM SOMAR POR EX: CE NO SALÁRIO VOCÊ POR 1 E NO ADICIONAL VOCÊ POR 3 ELE VAI TE RESPONDER 23 AO INVEZ DA SOMA. PARA ISSO DEVEMOS ADICIONAR int PARA INTEIROS E float PARA FLUTUANTE POR EX NO COD ABAIXO;

salario = int (input ("porfavor digite o quanto recebe"))

adicional = float (input ("digite o adicional"))
#repare bem que nestas variáveis na parte antes do input eu adicionei o tipo de valor, ex int ou float, e dps tbm adocionei o input a uma caixa o pondo no meio do () ex; (input("digite algo")) ja que o primeiro ( ce fecha com o último) e assim por diante.
saldo = salario + adicional 

print (saldo)

#______________________________________________

#OBS A DIFERENÇA DE INT PARA FLOAT E QUE INT SOMA TODOS OS NÚMEROS INTEIROS, E JA O FLOAT SOMA ATE OS CENTAVOS, CE VC PLR SOMENTE INT E DOS QUISER ADICIONAR UM VALOR POR EX; 1,50 ELE DARA ERRO POIS ESSES VALORES SAO PARA FLOAT