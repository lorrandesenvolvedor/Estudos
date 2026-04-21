# programação orientada a objetos, POO
# parte mais complexa porém fácil caso estudamos partes menores como as anteriores.
""" forma especial de programação mais próximo de como expresariamos coisas da vida real como outros tipos de programação, com ela podemos ter maneira distatinta de escrever nosso programas de forma mais simples.
como cê fossem uma ia, e algo com opções mais reais como um ser humano seria."""

"""
                       CONTEÚDO:
              • classe
              • objeto/instância 
              • atributo 
              • metodo
              
"""
# atributos das classes, atributos são as qualidades, diferencial de cada classe terá.
#ex; vamos criar uma classe chamada pessoas:

class pessoa:
        cidade = "padrão" 
        carro = "padrão"
        moto = "padrão"

# AGR vamos criar outra classe chamada homem.

class homem:
        nome = "Lorran"
        sexo = "Masculino"
        Corcabelo = "preto"
        
# agora vamos criar uma chamada mulher.

class mulher:
        nome = "vitória"
        sexo = "feminino"
        corcabelo = "preto"

""" aqui vemos por ex, em mulher temos os valores e as strings."""

# Trabalhando com métodos.
# oque são métodos? , métodos são as ações que os atributos irão fazer.

""" vamos criar o método carro e o atributo movimento, a pergunta e, que cê ele estiver em movimento ele virara um método deixando de ser um atributo"""
# ex;

class círculos:
         raio = 25.8
# agora vamos criar uma ação para raio.         
         
         def cauculaArea(self):
         # a self e uma instância essencial no python, sem ela toda variável valor ou dados daria erro. nesse exemplo usamos self em def cauculaArea(self): e em self.Area = 3.14 * (raio ** 2) que são as áreas essenciais e obrigatórios para não dar erro.
                  self.Area = 3.14 * (self.raio ** 2)
         
         # cauculando a altura.
         
         def cauculaVolume (self, altura):
         # estamos criando uma variável, um parâmetro dentro da função cauculaVolume, no caso está variável/paremetro e a altura.
                 self.Volume = 3.14 *(self.raio**2)*altura
                 #obs tudo isso e possível exatamente pela importância do método self.
                 
"""
               *** Método Construtor ***

"""
class retangulo:
        ladoA = None
        ladoB = None
        
        def __init__(self, lado_a, lado_b):
            self.lado_a = lado_a
            self.lado_b = lado_b
        
        def caucula_area (self):
                   return self.lado_a * self.lado_b
                   
        def caucula_perimetros(self):
                  return self.lado_a +2 * self.lado_b