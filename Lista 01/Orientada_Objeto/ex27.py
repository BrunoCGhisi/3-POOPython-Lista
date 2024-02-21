codigo = int(input("Qual seu codigo"))
nas = int(input("Qual sua data de nascimento (anos)"))
ing = int(input("Qual o ano de ingresso na empresa"))
ano = int(input("Qual o ano atual ? "))

'''Ter no mínimo 65 anos de idade. 

 - Ter trabalhado no mínimo 30 anos. 

 - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
'''
idade = ano - nas 
empresa = idade - ing
if idade > 60:
    print("Aposentado")
elif empresa > 30:
    print("Aposentado")
elif idade > 60 and empresa >25:
    print("Aposentado")
else:
    print("Não aposentado")
