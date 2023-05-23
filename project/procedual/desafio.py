from funcoes import cadastrar, login, listar

menu = """--Bem vindo--
[1] Cadastrar
[2] Login
[3] Listar
[4] Sair
Opção: """

if __name__ == '__main__':
    while True:
        opcao = input(menu)
        match opcao:
            case '1':
                qtnd = int(input('Quantidade de usuários: '))
                cadastrar(qtnd)
            case '2':            
                user = input('Usuário: ')
                passwd = input('Senha: ')
                if(login(user, passwd)):
                    print(f'Entrou com sucesso na conta {user}')
                else:
                    print('Senha ou Usuario errado(s)')
                break
            case '3':
                listar()        
            case '4':
                break