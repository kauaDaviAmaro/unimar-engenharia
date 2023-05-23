from functionClass import FileManager, User

# Menu incrivel (melhor que interface grafica)
menu = """--Bem vindo--
[1] Cadastrar
[2] Login
[3] Listar
[4] Sair
Opção: """

def main():
    # Loop top
    while True:
        # definindo o nome do arquivo (isto aqui é opcional)
        manager = FileManager("usuarios.txt")
        opcao = input(menu)

        # switch
        match opcao:
            case "1":
                user = User(input("Usuário: "), input("Senha: "))
                manager.register_user(user=user)
            case "2":
                user = User(input("Usuário: "), input("Senha: "))

                if manager.login_user(user=user):
                    print(f"Entrou com sucesso na conta {user.login}")
                else: 
                    print("Senha ou Usuario errado(s)")

            case "3":
                print(manager.display_user())
            case "4":
                break


if __name__ == "__main__":
    main()