# já que já sabemos criar arquivos, vamos escrever dentro dele.

def gerarArquivos ():
    arquivos = open("dados.txt","w")
    arquivo.close()
    
def escreveArquivos():
       
    arquivo = open("dados.txt", "a")# repare que invez de usarmos w usamos "a" pois assim podemos escrever dentro do arquivo. 
    #para podermos por o texto nele fazemos o seguinte comando:
    arquivo.write("texto de dentro do arquivo ")
        #aqui o arquivo.write e o responsável por digitar dentro do arquivo gerado.
        
    """podemos pegar e criar uma variável, assim colocamos ela no lugar do texto e oque for digitado no prompt será posto dentro do 📂 arquivo 📂 """ 

    arquivo.close() #para fechar novamente.
    
gerarArquivos()
escreveArquovo()