equipamentos = []
valores = []
seriais = []
setor = []
resposta = "S"
while resposta == "S":

    equipamentos.append(input("\n Insira o equipamento. "))
    valores.append(float(input("Qual o valor? ")))
    seriais.append(input("Qual o serial do equip? "))
    setor.append(input("Informe o setor. "))
    resposta = (input("\n Digite \"S\" para continuar. ")).upper()

busca = (input ("\nDigite o nome do equipamento que deseja buscar. "))
for indice in range(0,len(equipamentos)):
    if busca == equipamentos [indice]:
        print("Valor..", valores[indice])
        print("serial.", seriais[indice])
        print("setor.", setor[indice])

