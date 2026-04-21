

# primeiro ex o len, ele serve para conta a quantidade de caracter dentro da string.
curso = "programação em python"
aula = 15
print (len(curso))

#______________________________________________
# lower() serve para remover toda letra maiúscula de uma variável. por ex;
print (curso.lower())

#OBS O LOWER() E USADO DA SEGUINTE MANEIRA; print (curso.lower()) POIS TOMA CUIDADO PARA NÃO CONFUNDILO!

#______________________________________________
# upper() este ja e o oposto do lower() pois ele torna todo txt de uma variável maiúsculo! 
#usado da seguinte forma:
print (curso.upper())

#______________________________________________
#str() este método transforma tudo que esta em float ou int em string, para usalo e da seguinte maneira;
print (str(aula))
#agr também e possível sabe o tipo da variável pelo ex;
print (type(aula))
#desta forma ele puxa o valor e o tipo de variável.

#ENTAO SEGUINDO A LÓGICA PARA FAZER QUE TYPE FUNCIONE NESTE COD EU PRECISSO PUXAR O STR DENTRO DELE DA SEGUINTE MANEIRA;
print (type(str(aula)))
#desta forma acima, eu acabei de de fazer o tipo de valor que no caso esta na variável aula virar str. isso tabem pode ser feito de milhares de formas usando float, int, e outros,,,