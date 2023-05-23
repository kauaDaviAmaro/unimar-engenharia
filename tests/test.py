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
    def test_user_register(self) -> None:
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

    # Verifica o display da lista de usuarios
    def test_display_user(self) -> None:
        # Lista de usuarios 
        self.assertEqual(type(FileManager().display_user()), str)

    # deletar o arquivo ao concluir os testes
    def tearDown(self) -> None:
        FileManager().delete_file()
        return super().tearDown()