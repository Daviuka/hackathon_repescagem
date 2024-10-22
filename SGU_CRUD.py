import os 
usuario = {}

os.system('cls')
while True:
    print(30*'-', 'Menu de Gerenciamentos de Usuários', 30*'-')
    print('1. Cadastrar Usuário')
    print('2. Listar Usuário')
    print('3. Editar Usuário')
    print('4. Excluir Usuário')
    print('5. Sair do Sistema')
    print(96*'-')

    opcao = input('Digite a opcao que você deseja: ')

    # Cadastrar o Usuário
    if opcao == "1":
        nome = str(input('Digite o nome do usuário que você deseja: '))
        idade = int(input('Digite a idade do usuário: '))
        usuario[nome] = {'Nome': nome, 'Idade': idade}
        print(f'Usuário {nome} foi cadastrado com sucesso!')
    
    #Listar Usuário
    elif opcao == '2':
        if usuario:
            print('\n--- Lista de Usuários ---')
            for idade, dados in usuario.items():
                print(f'Nome: {dados['Nome']}, Idade: {dados['Idade']}')
        else:
            print('Nenhum usuário encontrado')

    #Editar Usuário
    elif opcao == '3':
        if usuario:
            print('\n--- Lista de Usuários ---')
            for idade, dados in usuario.items():
                print(f'Nome: {dados['Nome']}, Idade: {dados['Idade']}')
        nome = str(input('Digite um nome de usuário pra você editar: '))
        if nome in usuario:
            idade = int(input('Digite a nova idade: '))
            usuario[idade] = {'Nome': nome, 'Idade': idade}
            print(f'Usuário {nome} foi editado com sucesso!')
        else:
            print('Nenhum valor foi digitado!')
        

    #Excluir usuário
    elif opcao == '4':
        nome_remove = input('Digite o nome para remover: ')
        if nome_remove in usuario:
            del usuario[nome_remove]
            print('Usuário removido com sucesso!')
        else:
            print('Usuário não encontrado')

    #Sair do sistema
    elif opcao == '5':
        print('Saindo do Sistema...')
        break