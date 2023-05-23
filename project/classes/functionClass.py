import os

class User:
    # Criação do obj Para guardar os dados do usuário (e login)
    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self.password = password



class FileManager:
    # inicialização do Gerenciador
    def __init__(self, file_name: str = "user.txt") -> None:
        self.file_name = file_name
        
        if not self.file_exists(): 
            self.create_file()

    def delete_file(self) -> None:
        os.remove(self.file_name)

    def file_exists(self) -> bool:
        return os.path.exists(self.file_name)

    def create_file(self) -> None:
        with open(self.file_name, "w") as file:
            pass
    
    # Guarda usuario ☻
    def register_user(self, user: User) -> None:
        with open(self.file_name, "a") as file:
            file.write(f"{user.login}:{user.password}\n")

    # Verifica se o usuario existe ☻
    def login_user(self, user: User) -> bool:
        with open(self.file_name, "r") as file:
            for line in file:
                login, password = line.split(":")
                if user.login == login and user.password == password.strip():
                    return True
            return False

    # Lista todos os usuarios ☻
    def list_users(self) -> list[dict]:
        with open(self.file_name, "r") as file:
            all_users = []
            for line in file:
                login, passwd = line.split(":")
                all_users.append({login.strip(): passwd.strip()})
        return all_users

    # Mostra todos os usuarios ☻
    def display_user(self) -> str:
        text = ""
        for item in self.list_users():
            login, password = next(iter(item.items()))
            text += f"{login} - {password}\n"
        return text