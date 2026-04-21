# lendo arquivos em python 

def lerArquivo ():
    arquivo = open("dados.txt", "r") #aqui abre o arquivo
    
    line = arquivo.readline() #aqui vasculha as linhas do arquivo 
    while line != "": #aqui verifica cê a linha e branco cê for ele ignora
        print(line) #aqui printa o conteúdo da linha
        line = arquivo.readline() #aqui confirma a leitura 
        
    arquivo.close #aqui fecha o arquivo.

lerArquivo()