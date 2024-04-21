# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(683, 635)
        Login.setCursor(QCursor(Qt.PointingHandCursor))
        Login.setStyleSheet(u"background-color: rgb(0,74, 112);")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(130, 280, 441, 321))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_usuario = QLineEdit(self.frame)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(130, 30, 131, 31))
        sizePolicy.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy)
        self.txt_usuario.setCursor(QCursor(Qt.ArrowCursor))
        self.txt_usuario.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_usuario.setAlignment(Qt.AlignCenter)
        self.txt_usuario.setDragEnabled(False)
        self.txt_usuario.setReadOnly(False)
        self.txt_usuario.setClearButtonEnabled(False)
        self.txt_senha = QLineEdit(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(130, 90, 131, 31))
        sizePolicy.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy)
        self.txt_senha.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_senha.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.txt_senha.setAlignment(Qt.AlignCenter)
        self.chec_conectado = QCheckBox(self.frame)
        self.chec_conectado.setObjectName(u"chec_conectado")
        self.chec_conectado.setEnabled(True)
        self.chec_conectado.setGeometry(QRect(130, 150, 161, 41))
        sizePolicy.setHeightForWidth(self.chec_conectado.sizePolicy().hasHeightForWidth())
        self.chec_conectado.setSizePolicy(sizePolicy)
        self.chec_conectado.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(160, 230, 81, 31))
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")
        self.btn_login.setAutoDefault(False)
        self.frame_2 = QFrame(Login)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(150, 30, 381, 221))
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 10, 211, 211))
        self.label.setPixmap(QPixmap(u"imagens/homem-usuario.png"))
        self.label.setScaledContents(True)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio ou e-mail", None))
        self.txt_senha.setText(QCoreApplication.translate("Login", u"asdasdas", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.chec_conectado.setText(QCoreApplication.translate("Login", u"Mantenha-me conectado", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.label.setText("")
    # retranslateUi

