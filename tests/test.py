import unittest
from project.classes.functionClass import User, FileManager

# testa a classe User
class TestUser(unittest.TestCase):
    def test_user_creation(self):
        # testa se não tem erro na crição usuario 
        user = User("kaua", "davi")
        self.assertEqual(user.login, "kaua")
        self.assertEqual(user.password, "davi")

        user = User("Leo", "321")
        self.assertEqual(user.login, "Leo")
        self.assertEqual(user.password, "321")

# Testa a classe FileManager
manager = FileManager("Test")
class TestFileManger(unittest.TestCase):

    # cria arquivo
    def test_file_creation(self) -> None:
        manager.create_file()
        self.assertTrue(manager.file_exists())

    # Verifica se o usuario foi salvo no arquivo
    # def test_user_register(self) -> None:
    #     user = User("kaua", "davi")
    #     self.assertEqual(manager.register_user(user=user), None)

    # verifica se o usuario esta no arquivo
    def test_user_login(self) -> None:
        # cria o usario
        user = User("kaua", "davi")
        self.assertEqual(manager.register_user(user=user), None)

        # Login correto aqui :D (true)
        user = User("kaua", "davi")
        self.assertTrue(manager.login_user(user=user))

        # Essa aqui é para não logar :| (false)
        user = User("kaua", "senhaErrada")
        self.assertFalse(manager.login_user(user=user))
    
    # Verifica a lista de usuarios
    def test_user_list(self) -> None:
        # Lista de usuarios 
        self.assertEqual(type(manager.list_users()), list)

    # Verifica o display da lista de usuarios
    def test_display_user(self) -> None:
        # Lista de usuarios 
        self.assertEqual(type(manager.display_user()), str)
    
    def tearDownClass():
        manager.delete_file()