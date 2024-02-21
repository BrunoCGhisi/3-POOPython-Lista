homem = []
coisa = []

homem.append(int(input("idade do primeiro macho ")))
homem.append(int(input("idade do segundo macho ")))
while homem[0] == homem[1]:
    homem.remove(1)
    homem.append(int(input("idade do segundo macho ")))
coisa.append(int(input("Idade da primeira 'coisa' ")))
coisa.append(int(input("Idade da segunda 'coisa' ")))
while coisa[0] == coisa[1]:
    coisa.remove(1)
    coisa.append(int(input("idade do segundo 'coisa' ")))

homem.sort
coisa.sort
print(f"{homem[1]+coisa[0]}")
print(f"{homem[0]+coisa[1]}")




