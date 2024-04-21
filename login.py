
from PySide6.QtWidgets import QWidget, QMessageBox
from ui_login_2 import Ui_Login
from database import DataBase
import sys
from PySide6.QtCore import Qt


class Login(QWidget, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        self.btn_login.clicked.connect(self.checkLogin)
        

    def keyPressEvent(self, event):
    # Permitir que a tecla Enter também funcione para o botão de login
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.checkLogin()
            return  # Adiciona esse retorno para sair da função e evitar que o checkLogin seja chamado novamente
        else:
            super().keyPressEvent(event)


    def checkLogin(self):
        if not self.txt_usuario.text() or not self.txt_senha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('ERRO')
            msg.setText("Por favor, insira o nome de usuário e senha")
            msg.exec()
            return

        self.users = DataBase()
        self.users.connecta()
        
        usuario = self.txt_usuario.text()
        senha = self.txt_senha.text()
        
        tipo_usuario = self.users.check_user(usuario, senha)
        print("Tipo de usuário:", tipo_usuario)
        self.users.close_connection()
        if tipo_usuario:  
            print("Login bem sucedido!")
            from main import MainWindow
            self.w = MainWindow(tipo_usuario.lower())
            self.w.show()
            self.close()
        else:
            print("Login falhou!")
            if self.tentativas < 3:
                self.tentativas += 1
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f"Login ou senha incorretos \n\nTentativa: {self.tentativas} de 3")
                msg.exec()
            if self.tentativas == 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText("Número máximo de tentativas excedido. O aplicativo será encerrado.")
                msg.exec()
                sys.exit()