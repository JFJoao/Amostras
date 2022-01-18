nivel=input("Qual seu nivel de acesso, adm, user ou guest? ")
genero= input(" Qual seu genero ? ")
if nivel=="adm" and genero=="masculino":
    print(" Olá admnistrador")
elif nivel=="adm" and genero=="feminino":
    print("Ola admnistradora.")
elif nivel=="user" and genero=="masculino":
    print("Ola usuario")
elif nivel=="user" and genero=="feminino":
    print("Ola usuaria")
elif nivel=="guest" and genero=="masculino":
    print("Ola convidado")
elif nivel=="guest" and genero=="feminino":
    print("Ola convidada")
else:
    print("Ola desconhecido")