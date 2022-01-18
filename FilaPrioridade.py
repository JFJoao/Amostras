nome = input("digite seu nome:")
idade = int(input("digite sua idade: "))
doenca_infectocontagiosa = input("O paciente tem suspeita de doenca infectocontagiosa? ").upper()
if idade >= 65:
    print("O paciente " + nome + " tem prioridade no atendimento! ")
elif doenca_infectocontagiosa == "Sim":
    print ("O paciente "+nome+" deve aguardar na sala de espera reservada")
else:
    print("O paciente " + nome + " esta cadastrado, favor aguardar.")
    if idade <= 10:
        print("Paciente "+nome + " é uma criança.
