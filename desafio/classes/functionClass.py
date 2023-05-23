class User:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

class FileManager:
    def __init__(self, file_name: str = "user.txt"):
        self.file_name = file_name
    
    def register_user(self, user: User):
        with open(self.file_name, "a") as file:
            file.write(f"{user.login}:{user.password}\n")
        
    def login_user(self, user: User):
        with open(self.file_name, "r") as file:
            for line in file:
                login, password = line.split(":")
                if user.login == login and user.password == password.strip():
                    return True
            return False
    
    def list_users(self):
        with open(self.file_name, "r") as file:
            users = []
            for line in file:
                login = line.split(":")[0]
                users.append(login)
        return users