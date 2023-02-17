from elevador import Elevador


elevador = Elevador(5, 7)
  
while True:
    print(" (1) - Subir ")
    print(" (2) - Descer")
    opcao1 = input("\nSelecione sua opção: ")
    
    if opcao1 == "1":
        elevador.subir()

    elif opcao1 == "2":
        elevador.descer()

    else:
        print("Opção inválida tente novamente!")