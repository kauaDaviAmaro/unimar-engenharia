import unittest
from project.classes.functionClass import User, FileManager

# testa a classe User
class TestUser(unittest.TestCase):

    def test_user_creation(self):
        # testa se não ha erro na crição usuario 
        user = User("kaua", "davi")
        self.assertEqual(user.login, "kaua")
        self.assertEqual(user.password, "davi")

# Testa a classe FileManager
class TestFileManger(unittest.TestCase):

    # Verifica se o usuario foi salvo no arquivo
    def test_user_register(self):
        user = User("kaua", "davi")
        self.assertEqual(FileManager().register_user(user=user), None)

    # verifica se o usuario esta no arquivo
    def test_user_login(self) -> None:
        # Login correto aqui :D (true)
        user = User("kaua", "davi")
        self.assertTrue(FileManager().login_user(user=user))

        # Essa aqui é para não logar :| (false)
        user = User("kaua", "senhaErrada")
        self.assertFalse(FileManager().login_user(user=user))
    
    # Verifica a lista de usuarios
    def test_user_list(self) -> None:
        # Lista de usuarios 
        self.assertEqual(type(FileManager().list_users()), list)

    # # Apaga o arquivo
    # def tearDown(self) -> None:
    #     # os.remove(FileManager().file_name)
        
    #     # Retorna para o setUp()
    #     return super().tearDown()