""" vamos começar a criar arquivos externos em python, para isso vamos começar criando uma função."""

def criarArquivo():
    arquivo = open("dados.txt","w") # oque significa esse "w"? ele acha a abertura pra abrir um arquivo.
    
    # para fechar o arquivo devemos por o nome da variável + .close () da seguinte maneira,
    
    arquivo.close()

#agr iremos fechar essa função 
criarArquivos()