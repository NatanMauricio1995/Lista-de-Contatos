lista = {}

def menu():
    print("=" * 100)
    print(" "*48 + "MENU")
    print("=" * 100)
    print()
    print("Opções:")
    print(" 1 - Adicionar contato;")
    print(" 2 - Alterar contato;")
    print(" 3 - Remover contato;")
    print(" 4 - Listar contatos;")
    print(" 5 - Sair.\n")        
    
    opcao = 0
    
    while (opcao < 1) or (opcao > 5):
        try:
            opcao = int(input("Digite sua opção: "))
            if (opcao < 1) or (opcao > 5):
                print("Valor inválido! Insira novamente!\n")
        except ValueError:
            print("Erro: você deve digitar um número válido.\n")
        print("=" * 100, "\n\n")
       
    return opcao

def inserir_contato():
    global lista
    
    print("=" * 100)
    print(" "*42 + "INSERIR CONTATO")
    print("=" * 100)
    
    while True:
        nome = input("Insira o nome do contato: ").lower()
        if nome in lista:
            print("Contato já existe. Tente outro nome.\n")
        else:
            break
    
    telefone = input("Insira o número de telefone: ")
    lista[nome] = telefone
    print("Contato inserido com sucesso!\n")
    print("=" * 100, "\n\n")


def alterar_contato():
    global lista
    
    print("=" * 100)
    print(" "*42 + "ALTERAR CONTATO")
    print("=" * 100)
    
    while True:
        nome = input("Insira o nome do contato: ").lower()
        if nome not in lista:
            print("Contato não encontrado. Tente outro nome.\n")
        else:
            break
    
    telefone = input("Insira o novo número de telefone: ")
    lista[nome] = telefone
    print("Contato alterado com sucesso!\n")
    print("=" * 100, "\n\n")


def remover_contato():
    global lista
    
    print("=" * 100)
    print(" "*42 + "REMOVER CONTATO")
    print("=" * 100)
    
    while True:
        nome = input("Insira o nome do contato: ").lower()
        if nome not in lista:
            print("Contato não encontrado. Tente outro nome.\n")
        else:
            break
    
    del lista[nome]
    print(f"Contato '{nome.title()}' removido com sucesso!")
    print("=" * 100, "\n\n")
    
def exibir_contatos():
    print("=" * 100)
    print(" "*42 + "EXIBIR CONTATOS")
    print("=" * 100)
    
    if not lista:
        print("Nenhum contato cadastrado.")
    else:
        for nome, telefone in lista.items():
            print("Nome:", nome.title())
            print("Telefone:", telefone)
            print("-" * 30)
    print("=" * 100, "\n\n")

escolha = 0
while escolha != 5:
    escolha = menu()
    if (escolha == 1):
        inserir_contato()
    elif (escolha == 2):
        alterar_contato()
    elif (escolha == 3):
        remover_contato()
    elif (escolha == 4):
        exibir_contatos()
    else:
        print("Muito Obrigado! Até Mais!")