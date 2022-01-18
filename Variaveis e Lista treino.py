estoque=[]
adicionar="SIM"

while adicionar=="SIM":
    estoque.append(input("Item: "))
    estoque.append(float(input("Valor: ")))
    estoque.append(float(input("Quantidade: ")))
    estoque.append(input("Prateleira: "))
    adicionar=input ("Digite \"Sim\" para continuar"). upper()
    for elemento in estoque:
        print (elemento)

