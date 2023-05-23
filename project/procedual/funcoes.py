def cadastrar(qtnd) -> None:
    with open('usuarios.txt', 'a') as file:
        for i in range(qtnd):
            user = input(f'Nome do usuário {i+1}: ')
            passwd = input(f'Senha do usuário {i+1}: ')
            file.write(f'{user}:{passwd}\n')

def login(user, passwd) -> bool:
    with open('usuarios.txt', 'r') as file:
        for row in file:
            if user in row:
                senha_user = str(row[row.index(':')+1:]).strip()
                if passwd == senha_user:
                    return True
        return False

def listar() -> None:
    with open('usuarios.txt', 'r') as file:
        print('--lista de usuarios--')
        print(file.read())
        input('aperte enter para continuar')