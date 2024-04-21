# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maine3.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDateTimeEdit, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableView, QToolButton,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1794, 996)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(u"P\u00e1gina principal")
#endif // QT_CONFIG(tooltip)
        self.btn_home.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btn_home)

        self.btn_verificar_estoque = QPushButton(self.frame)
        self.btn_verificar_estoque.setObjectName(u"btn_verificar_estoque")
#if QT_CONFIG(tooltip)
        self.btn_verificar_estoque.setToolTip(u"Verifica o estoque")
#endif // QT_CONFIG(tooltip)
        self.btn_verificar_estoque.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btn_verificar_estoque)

        self.btn_cadastrar_produto = QPushButton(self.frame)
        self.btn_cadastrar_produto.setObjectName(u"btn_cadastrar_produto")
#if QT_CONFIG(tooltip)
        self.btn_cadastrar_produto.setToolTip(u"Cadastra produtos")
#endif // QT_CONFIG(tooltip)
        self.btn_cadastrar_produto.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btn_cadastrar_produto)

        self.btn_cadastro_usuario = QPushButton(self.frame)
        self.btn_cadastro_usuario.setObjectName(u"btn_cadastro_usuario")
#if QT_CONFIG(tooltip)
        self.btn_cadastro_usuario.setToolTip(u"<html><head/><body><p>Cadastra um usu\u00e1rio</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.btn_cadastro_usuario.setToolTipDuration(-1)
        self.btn_cadastro_usuario.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btn_cadastro_usuario)

        self.btn_clientes = QPushButton(self.frame)
        self.btn_clientes.setObjectName(u"btn_clientes")
#if QT_CONFIG(tooltip)
        self.btn_clientes.setToolTip(u"Exibe os clientes")
#endif // QT_CONFIG(tooltip)
        self.btn_clientes.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btn_clientes)

        self.btn_configuracoes = QPushButton(self.frame)
        self.btn_configuracoes.setObjectName(u"btn_configuracoes")
#if QT_CONFIG(tooltip)
        self.btn_configuracoes.setToolTip(u"Exibe as configura\u00e7\u00f5es do sistema")
#endif // QT_CONFIG(tooltip)
        self.btn_configuracoes.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btn_configuracoes)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
#if QT_CONFIG(tooltip)
        self.btn_contato.setToolTip(u"Exibe as informa\u00e7\u00f5es de contato do desenvolvedor do sistema")
#endif // QT_CONFIG(tooltip)
        self.btn_contato.setToolTipDuration(-1)
        self.btn_contato.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btn_contato)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy)
        self.Pages.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.home_pag = QWidget()
        self.home_pag.setObjectName(u"home_pag")
        self.verticalLayout_5 = QVBoxLayout(self.home_pag)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.home_pag)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 240, 651, 391))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_imagem = QLabel(self.frame_5)
        self.label_imagem.setObjectName(u"label_imagem")
        self.label_imagem.setGeometry(QRect(380, 40, 351, 321))
        self.label_imagem.setPixmap(QPixmap(u"../../Downloads/sistema-de-gerenciamento-de-conteudo.png"))
        self.label_imagem.setScaledContents(True)
        self.label_bem_vindo = QLabel(self.frame_5)
        self.label_bem_vindo.setObjectName(u"label_bem_vindo")
        self.label_bem_vindo.setGeometry(QRect(370, 370, 331, 61))
        self.label_bem_vindo.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.frame_5)

        self.Pages.addWidget(self.home_pag)
        self.page_estoque = QWidget()
        self.page_estoque.setObjectName(u"page_estoque")
        self.horizontalLayout_7 = QHBoxLayout(self.page_estoque)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tb_base = QTabWidget(self.page_estoque)
        self.tb_base.setObjectName(u"tb_base")
        self.tb_base.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.tb_base.setTabShape(QTabWidget.Triangular)
        self.tables_estoque = QWidget()
        self.tables_estoque.setObjectName(u"tables_estoque")
        self.verticalLayout_3 = QVBoxLayout(self.tables_estoque)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.linha_de_abrir_planilha = QLineEdit(self.tables_estoque)
        self.linha_de_abrir_planilha.setObjectName(u"linha_de_abrir_planilha")
        self.linha_de_abrir_planilha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.linha_de_abrir_planilha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.linha_de_abrir_planilha)

        self.btn_abrir_planilha = QPushButton(self.tables_estoque)
        self.btn_abrir_planilha.setObjectName(u"btn_abrir_planilha")
        self.btn_abrir_planilha.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_3.addWidget(self.btn_abrir_planilha)

        self.progressBar = QProgressBar(self.tables_estoque)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid grey; /* Borda da barra de progresso */\n"
"    border-radius: 5px; /* Cantos arredondados */\n"
"    background-color: white; /* Cor de fundo da barra de progresso */\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: green; /* Cor da barra de progresso */\n"
"}\n"
"")
        self.progressBar.setValue(0)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.label_estoque = QLabel(self.tables_estoque)
        self.label_estoque.setObjectName(u"label_estoque")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_estoque.sizePolicy().hasHeightForWidth())
        self.label_estoque.setSizePolicy(sizePolicy1)
        self.label_estoque.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.label_estoque)

        self.tabela_estoque = QTreeWidget(self.tables_estoque)
        self.tabela_estoque.setObjectName(u"tabela_estoque")

        self.verticalLayout_3.addWidget(self.tabela_estoque)

        self.frame_3 = QFrame(self.tables_estoque)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_importar = QPushButton(self.frame_3)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_4.addWidget(self.btn_importar)

        self.btn_gerar_saida = QPushButton(self.frame_3)
        self.btn_gerar_saida.setObjectName(u"btn_gerar_saida")
        self.btn_gerar_saida.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_4.addWidget(self.btn_gerar_saida)

        self.btn_estorno = QPushButton(self.frame_3)
        self.btn_estorno.setObjectName(u"btn_estorno")
        self.btn_estorno.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_4.addWidget(self.btn_estorno)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.label_saida = QLabel(self.tables_estoque)
        self.label_saida.setObjectName(u"label_saida")
        sizePolicy1.setHeightForWidth(self.label_saida.sizePolicy().hasHeightForWidth())
        self.label_saida.setSizePolicy(sizePolicy1)
        self.label_saida.setMinimumSize(QSize(0, 0))
        self.label_saida.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.label_saida)

        self.tabela_saida = QTreeWidget(self.tables_estoque)
        self.tabela_saida.setObjectName(u"tabela_saida")

        self.verticalLayout_3.addWidget(self.tabela_saida)

        self.tb_base.addTab(self.tables_estoque, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.label_estoque_2 = QLabel(self.tab_2)
        self.label_estoque_2.setObjectName(u"label_estoque_2")
        self.label_estoque_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.label_estoque_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.btn_grafico = QPushButton(self.tab_2)
        self.btn_grafico.setObjectName(u"btn_grafico")
        self.btn_grafico.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.btn_grafico)

        self.btn_excel = QPushButton(self.tab_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.btn_excel)

        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.txt_filtro)

        self.line = QFrame(self.tab_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalSpacer_4 = QSpacerItem(100, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.tableView = QTableView(self.tab_2)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        self.tb_base.addTab(self.tab_2, "")

        self.horizontalLayout_7.addWidget(self.tb_base)

        self.Pages.addWidget(self.page_estoque)
        self.pg_cadastrar_produto = QWidget()
        self.pg_cadastrar_produto.setObjectName(u"pg_cadastrar_produto")
        self.frame_2 = QFrame(self.pg_cadastrar_produto)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, -110, 1631, 1081))
        self.frame_2.setInputMethodHints(Qt.ImhNone)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_cadastramento_produtos = QLabel(self.frame_2)
        self.label_cadastramento_produtos.setObjectName(u"label_cadastramento_produtos")
        self.label_cadastramento_produtos.setGeometry(QRect(55, 160, 991, 61))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_cadastramento_produtos.sizePolicy().hasHeightForWidth())
        self.label_cadastramento_produtos.setSizePolicy(sizePolicy2)
        self.label_cadastramento_produtos.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 5px solid white;\n"
"}\n"
"\n"
"")
        self.label_produto = QLabel(self.frame_2)
        self.label_produto.setObjectName(u"label_produto")
        self.label_produto.setGeometry(QRect(32, 271, 51, 16))
        self.label_produto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_quantidade = QLabel(self.frame_2)
        self.label_quantidade.setObjectName(u"label_quantidade")
        self.label_quantidade.setGeometry(QRect(30, 340, 71, 16))
        self.label_quantidade.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_valor_produto = QLabel(self.frame_2)
        self.label_valor_produto.setObjectName(u"label_valor_produto")
        self.label_valor_produto.setGeometry(QRect(12, 406, 121, 20))
        self.label_valor_produto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_valor_unidade = QLabel(self.frame_2)
        self.label_valor_unidade.setObjectName(u"label_valor_unidade")
        self.label_valor_unidade.setGeometry(QRect(20, 470, 101, 16))
        self.label_valor_unidade.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_desconto = QLabel(self.frame_2)
        self.label_desconto.setObjectName(u"label_desconto")
        self.label_desconto.setGeometry(QRect(32, 541, 61, 16))
        self.label_desconto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_data_compra = QLabel(self.frame_2)
        self.label_data_compra.setObjectName(u"label_data_compra")
        self.label_data_compra.setGeometry(QRect(18, 608, 91, 20))
        self.label_data_compra.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_codigo_item = QLabel(self.frame_2)
        self.label_codigo_item.setObjectName(u"label_codigo_item")
        self.label_codigo_item.setGeometry(QRect(14, 675, 91, 20))
        self.label_codigo_item.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_cliente_2 = QLabel(self.frame_2)
        self.label_cliente_2.setObjectName(u"label_cliente_2")
        self.label_cliente_2.setGeometry(QRect(32, 741, 51, 16))
        self.label_cliente_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.label_descricao_produto = QLabel(self.frame_2)
        self.label_descricao_produto.setObjectName(u"label_descricao_produto")
        self.label_descricao_produto.setGeometry(QRect(10, 810, 131, 20))
        self.label_descricao_produto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.txt_produto = QLineEdit(self.frame_2)
        self.txt_produto.setObjectName(u"txt_produto")
        self.txt_produto.setGeometry(QRect(140, 265, 171, 25))
        self.txt_produto.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_quantidade = QLineEdit(self.frame_2)
        self.txt_quantidade.setObjectName(u"txt_quantidade")
        self.txt_quantidade.setGeometry(QRect(140, 335, 171, 25))
        self.txt_quantidade.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_valor_produto = QLineEdit(self.frame_2)
        self.txt_valor_produto.setObjectName(u"txt_valor_produto")
        self.txt_valor_produto.setGeometry(QRect(140, 405, 171, 25))
        self.txt_valor_produto.setContextMenuPolicy(Qt.NoContextMenu)
        self.txt_valor_produto.setAutoFillBackground(False)
        self.txt_valor_produto.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_valor_produto.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.txt_valor_produto.setClearButtonEnabled(False)
        self.txt_unidade = QLineEdit(self.frame_2)
        self.txt_unidade.setObjectName(u"txt_unidade")
        self.txt_unidade.setGeometry(QRect(140, 465, 171, 25))
        self.txt_unidade.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_unidade.setInputMethodHints(Qt.ImhPreferNumbers)
        self.txt_unidade.setInputMask(u"")
        self.txt_unidade.setDragEnabled(False)
        self.txt_unidade.setReadOnly(False)
        self.txt_desconto = QLineEdit(self.frame_2)
        self.txt_desconto.setObjectName(u"txt_desconto")
        self.txt_desconto.setGeometry(QRect(140, 537, 171, 25))
        self.txt_desconto.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_codigo_item = QLineEdit(self.frame_2)
        self.txt_codigo_item.setObjectName(u"txt_codigo_item")
        self.txt_codigo_item.setGeometry(QRect(140, 675, 171, 25))
        self.txt_codigo_item.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_cliente = QLineEdit(self.frame_2)
        self.txt_cliente.setObjectName(u"txt_cliente")
        self.txt_cliente.setGeometry(QRect(140, 735, 171, 25))
        self.txt_cliente.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.txt_descricao_produto = QLineEdit(self.frame_2)
        self.txt_descricao_produto.setObjectName(u"txt_descricao_produto")
        self.txt_descricao_produto.setGeometry(QRect(140, 810, 171, 25))
        self.txt_descricao_produto.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")
        self.btn_adicionar_produto = QPushButton(self.frame_2)
        self.btn_adicionar_produto.setObjectName(u"btn_adicionar_produto")
        self.btn_adicionar_produto.setGeometry(QRect(400, 270, 141, 23))
        self.btn_adicionar_produto.setStyleSheet(u"QPushButton {\n"
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
        icon = QIcon()
        icon.addFile(u"../../Downloads/pngwing.com.png", QSize(), QIcon.Active, QIcon.On)
        self.btn_adicionar_produto.setIcon(icon)
        self.btn_atualizar_produto = QPushButton(self.frame_2)
        self.btn_atualizar_produto.setObjectName(u"btn_atualizar_produto")
        self.btn_atualizar_produto.setGeometry(QRect(400, 316, 141, 23))
        self.btn_atualizar_produto.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u"../../Downloads/toppng.com-update-512x512.png", QSize(), QIcon.Active, QIcon.On)
        self.btn_atualizar_produto.setIcon(icon1)
        self.btn_limpar_campos = QPushButton(self.frame_2)
        self.btn_limpar_campos.setObjectName(u"btn_limpar_campos")
        self.btn_limpar_campos.setGeometry(QRect(400, 409, 141, 23))
        self.btn_limpar_campos.setMouseTracking(False)
        self.btn_limpar_campos.setAcceptDrops(False)
        self.btn_limpar_campos.setAutoFillBackground(False)
        self.btn_limpar_campos.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u"../../Downloads/1486564399-close_81512.png", QSize(), QIcon.Active, QIcon.On)
        self.btn_limpar_campos.setIcon(icon2)
        self.btn_confirmar = QPushButton(self.frame_2)
        self.btn_confirmar.setObjectName(u"btn_confirmar")
        self.btn_confirmar.setGeometry(QRect(400, 600, 141, 23))
        self.btn_confirmar.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255); /* Cor do texto (branco) */\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 200, 100), stop:1 rgb(150, 255, 150)); /* Gradiente de verde claro para verde mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(150, 255, 150), stop:1 rgb(200, 255, 200)); /* Gradiente de verde mais claro para verde ainda mais claro */\n"
"    color: rgb(0, 0, 0); /* Cor do texto (preto) */\n"
"}\n"
"")
        self.btn_ver_item = QPushButton(self.frame_2)
        self.btn_ver_item.setObjectName(u"btn_ver_item")
        self.btn_ver_item.setGeometry(QRect(400, 660, 141, 31))
        self.btn_ver_item.setMinimumSize(QSize(141, 0))
        self.btn_ver_item.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u"../../Downloads/pasta.png", QSize(), QIcon.Active, QIcon.On)
        self.btn_ver_item.setIcon(icon3)
        self.frame_valor_total_produtos = QFrame(self.frame_2)
        self.frame_valor_total_produtos.setObjectName(u"frame_valor_total_produtos")
        self.frame_valor_total_produtos.setGeometry(QRect(710, 260, 335, 101))
        self.frame_valor_total_produtos.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_valor_total_produtos.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_total_produtos.setFrameShadow(QFrame.Raised)
        self.label_valor_total_produtos = QLabel(self.frame_valor_total_produtos)
        self.label_valor_total_produtos.setObjectName(u"label_valor_total_produtos")
        self.label_valor_total_produtos.setGeometry(QRect(2, 10, 321, 31))
        self.label_valor_total_produtos.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.frame_quantidade = QFrame(self.frame_2)
        self.frame_quantidade.setObjectName(u"frame_quantidade")
        self.frame_quantidade.setGeometry(QRect(710, 700, 335, 101))
        self.frame_quantidade.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_quantidade.setFrameShape(QFrame.StyledPanel)
        self.frame_quantidade.setFrameShadow(QFrame.Raised)
        self.label_quantidade_2 = QLabel(self.frame_quantidade)
        self.label_quantidade_2.setObjectName(u"label_quantidade_2")
        self.label_quantidade_2.setGeometry(QRect(20, 10, 301, 31))
        self.label_quantidade_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.dateEdit = QDateEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(140, 605, 171, 25))
        self.dateEdit.setStyleSheet(u"QDateEdit {\n"
"    color: #333; /* Cor do texto */\n"
"    background-color: white; /* Cor de fundo */\n"
"}\n"
"")
        self.dateEdit.setInputMethodHints(Qt.ImhPreferNumbers)
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setMinimumDate(QDate(1900, 9, 14))
        self.dateEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setTimeSpec(Qt.UTC)
        self.frame_valor_desconto = QFrame(self.frame_2)
        self.frame_valor_desconto.setObjectName(u"frame_valor_desconto")
        self.frame_valor_desconto.setGeometry(QRect(710, 550, 335, 101))
        self.frame_valor_desconto.setStyleSheet(u"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_valor_desconto.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_desconto.setFrameShadow(QFrame.Raised)
        self.label_valor_desconto = QLabel(self.frame_valor_desconto)
        self.label_valor_desconto.setObjectName(u"label_valor_desconto")
        self.label_valor_desconto.setGeometry(QRect(2, 10, 331, 32))
        self.label_valor_desconto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.btn_carregar_imagem = QPushButton(self.frame_2)
        self.btn_carregar_imagem.setObjectName(u"btn_carregar_imagem")
        self.btn_carregar_imagem.setGeometry(QRect(390, 550, 161, 23))
        self.btn_carregar_imagem.setStyleSheet(u"QPushButton {\n"
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
        self.frame_imagem = QFrame(self.frame_2)
        self.frame_imagem.setObjectName(u"frame_imagem")
        self.frame_imagem.setGeometry(QRect(1159, 270, 321, 331))
        self.frame_imagem.setFrameShape(QFrame.StyledPanel)
        self.frame_imagem.setFrameShadow(QFrame.Raised)
        self.frame_valor_do_desconto = QFrame(self.frame_2)
        self.frame_valor_do_desconto.setObjectName(u"frame_valor_do_desconto")
        self.frame_valor_do_desconto.setGeometry(QRect(710, 400, 335, 101))
        self.frame_valor_do_desconto.setStyleSheet(u"\n"
"background-color: rgb(100, 200, 100); /* Verde claro */\n"
"")
        self.frame_valor_do_desconto.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_do_desconto.setFrameShadow(QFrame.Raised)
        self.label_valor_do_desconto = QLabel(self.frame_valor_do_desconto)
        self.label_valor_do_desconto.setObjectName(u"label_valor_do_desconto")
        self.label_valor_do_desconto.setGeometry(QRect(47, 8, 231, 41))
        self.label_valor_do_desconto.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"}\n"
"")
        self.btn_mais_opcoes = QToolButton(self.frame_2)
        self.btn_mais_opcoes.setObjectName(u"btn_mais_opcoes")
        self.btn_mais_opcoes.setGeometry(QRect(20, 120, 121, 25))
        self.btn_mais_opcoes.setBaseSize(QSize(0, 0))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(50, 150, 250, 255))
        gradient.setColorAt(1, QColor(100, 200, 255, 255))
        brush1 = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        gradient1 = QLinearGradient(0, 0, 0, 1)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(50, 150, 250, 255))
        gradient1.setColorAt(1, QColor(100, 200, 255, 255))
        brush2 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        gradient2 = QLinearGradient(0, 0, 0, 1)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(50, 150, 250, 255))
        gradient2.setColorAt(1, QColor(100, 200, 255, 255))
        brush3 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gradient3 = QLinearGradient(0, 0, 0, 1)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(50, 150, 250, 255))
        gradient3.setColorAt(1, QColor(100, 200, 255, 255))
        brush4 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        gradient4 = QLinearGradient(0, 0, 0, 1)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(50, 150, 250, 255))
        gradient4.setColorAt(1, QColor(100, 200, 255, 255))
        brush5 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        gradient5 = QLinearGradient(0, 0, 0, 1)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(50, 150, 250, 255))
        gradient5.setColorAt(1, QColor(100, 200, 255, 255))
        brush6 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        gradient6 = QLinearGradient(0, 0, 0, 1)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(50, 150, 250, 255))
        gradient6.setColorAt(1, QColor(100, 200, 255, 255))
        brush7 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        gradient7 = QLinearGradient(0, 0, 0, 1)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(50, 150, 250, 255))
        gradient7.setColorAt(1, QColor(100, 200, 255, 255))
        brush8 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        gradient8 = QLinearGradient(0, 0, 0, 1)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(50, 150, 250, 255))
        gradient8.setColorAt(1, QColor(100, 200, 255, 255))
        brush9 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        self.btn_mais_opcoes.setPalette(palette)
        self.btn_mais_opcoes.setAcceptDrops(False)
        self.btn_mais_opcoes.setStyleSheet(u"QToolButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    font-size: 16px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */\n"
"    border: 3px solid transparent;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */\n"
"    color: black;\n"
"}\n"
"")
        self.btn_mais_opcoes.setInputMethodHints(Qt.ImhNone)
        self.btn_mais_opcoes.setAutoRepeatDelay(305)
        self.btn_mais_opcoes.setPopupMode(QToolButton.MenuButtonPopup)
        self.btn_mais_opcoes.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.btn_mais_opcoes.setAutoRaise(False)
        self.btn_mais_opcoes.setArrowType(Qt.DownArrow)
        self.btn_editar = QPushButton(self.frame_2)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setGeometry(QRect(400, 361, 141, 23))
        sizePolicy.setHeightForWidth(self.btn_editar.sizePolicy().hasHeightForWidth())
        self.btn_editar.setSizePolicy(sizePolicy)
        self.btn_editar.setStyleSheet(u"QPushButton {\n"
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
        self.Pages.addWidget(self.pg_cadastrar_produto)
        self.pg_cliente = QWidget()
        self.pg_cliente.setObjectName(u"pg_cliente")
        self.frame_6 = QFrame(self.pg_cliente)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(-1, -1, 1651, 991))
        self.frame_6.setToolTipDuration(0)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(360, 110, 71, 41))
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 5px solid white;\n"
"}\n"
"\n"
"")
        self.Pages.addWidget(self.pg_cliente)
        self.pg_cadastro_usuario = QWidget()
        self.pg_cadastro_usuario.setObjectName(u"pg_cadastro_usuario")
        self.pg_cadastro_usuario.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.verticalLayout_6 = QVBoxLayout(self.pg_cadastro_usuario)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_tela = QLabel(self.pg_cadastro_usuario)
        self.label_tela.setObjectName(u"label_tela")
        self.label_tela.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 5px solid white;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.label_tela)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.label_cadastro = QLabel(self.pg_cadastro_usuario)
        self.label_cadastro.setObjectName(u"label_cadastro")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_cadastro.sizePolicy().hasHeightForWidth())
        self.label_cadastro.setSizePolicy(sizePolicy3)
        self.label_cadastro.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"	border: 3px solid white;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.label_cadastro)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.txt_usuario = QLineEdit(self.pg_cadastro_usuario)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.gridLayout.addWidget(self.txt_usuario, 0, 4, 1, 1)

        self.txt_nome = QLineEdit(self.pg_cadastro_usuario)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.gridLayout.addWidget(self.txt_nome, 0, 2, 1, 1)

        self.label_nome = QLabel(self.pg_cadastro_usuario)
        self.label_nome.setObjectName(u"label_nome")

        self.gridLayout.addWidget(self.label_nome, 0, 1, 1, 1)

        self.label_usuario = QLabel(self.pg_cadastro_usuario)
        self.label_usuario.setObjectName(u"label_usuario")

        self.gridLayout.addWidget(self.label_usuario, 0, 3, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_cpf = QLabel(self.pg_cadastro_usuario)
        self.label_cpf.setObjectName(u"label_cpf")

        self.horizontalLayout_3.addWidget(self.label_cpf)

        self.txt_cpf = QLineEdit(self.pg_cadastro_usuario)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.txt_cpf)

        self.label_endereco = QLabel(self.pg_cadastro_usuario)
        self.label_endereco.setObjectName(u"label_endereco")

        self.horizontalLayout_3.addWidget(self.label_endereco)

        self.txt_endereco = QLineEdit(self.pg_cadastro_usuario)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.txt_endereco)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_email = QLabel(self.pg_cadastro_usuario)
        self.label_email.setObjectName(u"label_email")

        self.horizontalLayout_5.addWidget(self.label_email)

        self.txt_email = QLineEdit(self.pg_cadastro_usuario)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.txt_email)

        self.label_estado = QLabel(self.pg_cadastro_usuario)
        self.label_estado.setObjectName(u"label_estado")

        self.horizontalLayout_5.addWidget(self.label_estado)

        self.txt_estado = QLineEdit(self.pg_cadastro_usuario)
        self.txt_estado.setObjectName(u"txt_estado")
        self.txt_estado.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.txt_estado)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_numero = QLabel(self.pg_cadastro_usuario)
        self.label_numero.setObjectName(u"label_numero")

        self.horizontalLayout_6.addWidget(self.label_numero)

        self.txt_numero = QLineEdit(self.pg_cadastro_usuario)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.txt_numero)

        self.label_cep = QLabel(self.pg_cadastro_usuario)
        self.label_cep.setObjectName(u"label_cep")

        self.horizontalLayout_6.addWidget(self.label_cep)

        self.txt_cep = QLineEdit(self.pg_cadastro_usuario)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.txt_cep)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_senha = QLabel(self.pg_cadastro_usuario)
        self.label_senha.setObjectName(u"label_senha")

        self.horizontalLayout_9.addWidget(self.label_senha)

        self.txt_senha = QLineEdit(self.pg_cadastro_usuario)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.txt_senha)

        self.label_confirmar_senha = QLabel(self.pg_cadastro_usuario)
        self.label_confirmar_senha.setObjectName(u"label_confirmar_senha")

        self.horizontalLayout_9.addWidget(self.label_confirmar_senha)

        self.txt_confirmar_senha = QLineEdit(self.pg_cadastro_usuario)
        self.txt_confirmar_senha.setObjectName(u"txt_confirmar_senha")
        self.txt_confirmar_senha.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */\n"
"    border: 2px solid rgb(50, 150, 250); /* Borda azul */\n"
"    border-radius: 6px; /* Cantos arredondados */\n"
"    padding: 3px; /* Espa\u00e7amento interno */\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.txt_confirmar_senha)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_perfil = QLabel(self.pg_cadastro_usuario)
        self.label_perfil.setObjectName(u"label_perfil")
        self.label_perfil.setEnabled(True)

        self.horizontalLayout_11.addWidget(self.label_perfil)

        self.comboBox = QComboBox(self.pg_cadastro_usuario)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #999;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    selection-background-color: #ddd;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"    width: 20px; /* Aumenta a largura do bot\u00e3o de dropdown */\n"
"    border-left: 1px solid #999; /* Adiciona uma borda \u00e0 esquerda do bot\u00e3o de dropdown */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                      stop:0 #eee, stop:1 #ddd);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(down_arrow.png); /* \u00cdcone do bot\u00e3o de dropdown */\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.comboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(200, 500, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.btn_fazer_cadastro = QPushButton(self.pg_cadastro_usuario)
        self.btn_fazer_cadastro.setObjectName(u"btn_fazer_cadastro")
        self.btn_fazer_cadastro.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_6.addWidget(self.btn_fazer_cadastro)

        self.Pages.addWidget(self.pg_cadastro_usuario)
        self.pg_configuracoes = QWidget()
        self.pg_configuracoes.setObjectName(u"pg_configuracoes")
        self.label_configuracoes = QLabel(self.pg_configuracoes)
        self.label_configuracoes.setObjectName(u"label_configuracoes")
        self.label_configuracoes.setGeometry(QRect(310, 230, 291, 161))
        self.Pages.addWidget(self.pg_configuracoes)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.frame_4 = QFrame(self.pg_contato)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-240, -260, 1911, 1251))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(600, 360, 411, 101))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"\n"
"}\n"
"\n"
"")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(660, 480, 41, 31))
        self.label_3.setPixmap(QPixmap(u"../../Downloads/Whatsapp_37229.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(710, 490, 151, 16))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"\n"
"}\n"
"\n"
"")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(660, 530, 41, 31))
        self.label_5.setPixmap(QPixmap(u"../../Downloads/linkedin_icon-icons.com_65929.png"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(710, 535, 251, 20))
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    text-align: center; /* Centraliza o texto horizontalmente */\n"
"    vertical-align: middle; /* Centraliza o texto verticalmente */\n"
"\n"
"}\n"
"\n"
"")
        self.Pages.addWidget(self.pg_contato)

        self.gridLayout_2.addWidget(self.Pages, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(2)
        self.tb_base.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_verificar_estoque.setText(QCoreApplication.translate("MainWindow", u"Verificar estoque", None))
        self.btn_cadastrar_produto.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Produto", None))
        self.btn_cadastro_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_configuracoes.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; vertical-align:super;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; vertical-align:super;\"><br/>SISTEMA DE GERENCIAMENTO </span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; vertical-align:super;\">DO CONTROLE DE ESTOQUE</span></p></body></html>", None))
        self.label_imagem.setText("")
        self.label_bem_vindo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#ffffff;\">Bem vindo(a) ao</span></p></body></html>", None))
        self.linha_de_abrir_planilha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"O arquivo excel aparecer\u00e1 aqui", None))
        self.btn_abrir_planilha.setText(QCoreApplication.translate("MainWindow", u"Abrir Planilha", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.label_estoque.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">ESTOQUE</span></p></body></html>", None))
        ___qtreewidgetitem = self.tabela_estoque.headerItem()
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Cod Item", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Data da compra", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Valor da unidade", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Valor do produto", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Produto", None));
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_gerar_saida.setText(QCoreApplication.translate("MainWindow", u"Gerar Sa\u00edda", None))
        self.btn_estorno.setText(QCoreApplication.translate("MainWindow", u"Estorno", None))
        self.label_saida.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">SA\u00cdDA</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tabela_saida.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Cod produto", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data cria\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Data sa\u00edda", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Produto", None));
        self.tb_base.setTabText(self.tb_base.indexOf(self.tables_estoque), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_estoque_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; font-style:italic;\">ESTOQUE</span></p></body></html>", None))
        self.btn_grafico.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.tb_base.setTabText(self.tb_base.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.label_cadastramento_produtos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Cadastramento de Produtos</span></p></body></html>", None))
        self.label_produto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Produto</span></p></body></html>", None))
        self.label_quantidade.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Quantidade</span></p></body></html>", None))
        self.label_valor_produto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Valor real do produto</span></p></body></html>", None))
        self.label_valor_unidade.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Valor da Unidade</span></p></body></html>", None))
        self.label_desconto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Desconto</span></p></body></html>", None))
        self.label_data_compra.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Data da Compra</span></p><p><br/></p></body></html>", None))
        self.label_codigo_item.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">C\u00f3digo do Item</span></p></body></html>", None))
        self.label_cliente_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Cliente</span></p></body></html>", None))
        self.label_descricao_produto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Descri\u00e7\u00e3o do produto</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.txt_valor_produto.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.txt_valor_produto.setText("")
        self.txt_valor_produto.setPlaceholderText("")
        self.txt_unidade.setText("")
        self.txt_unidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Opcional", None))
#if QT_CONFIG(tooltip)
        self.btn_adicionar_produto.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/pngwing.com.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_adicionar_produto.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR", None))
        self.btn_atualizar_produto.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
        self.btn_limpar_campos.setText(QCoreApplication.translate("MainWindow", u"APAGAR", None))
        self.btn_confirmar.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR", None))
        self.btn_ver_item.setText(QCoreApplication.translate("MainWindow", u"VER ITEM", None))
        self.label_valor_total_produtos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Valor total do produtos</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_quantidade_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Quantidade total de produtos</span></p></body></html>", None))
        self.label_valor_desconto.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Valor do produto com desconto</span></p></body></html>", None))
        self.btn_carregar_imagem.setText(QCoreApplication.translate("MainWindow", u"CARREGAR IMAGEM", None))
        self.label_valor_do_desconto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Valor do desconto</span></p></body></html>", None))
        self.btn_mais_opcoes.setText(QCoreApplication.translate("MainWindow", u"Mais op\u00e7\u00f5es...", None))
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"EDITAR ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.label_tela.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; font-style:italic;\">TELA PARA CADASTRAMENTO DE USU\u00c1RIO</span></p></body></html>", None))
        self.label_cadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Cadastrar Usu\u00e1rio</span></p></body></html>", None))
        self.label_nome.setText(QCoreApplication.translate("MainWindow", u"NOME:", None))
        self.label_usuario.setText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIO:", None))
        self.label_cpf.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.label_endereco.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O:", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"E-MAIL:", None))
        self.label_estado.setText(QCoreApplication.translate("MainWindow", u"ESTADO:", None))
        self.label_numero.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO:", None))
        self.label_cep.setText(QCoreApplication.translate("MainWindow", u"CEP:", None))
        self.label_senha.setText(QCoreApplication.translate("MainWindow", u"SENHA:", None))
        self.label_confirmar_senha.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR SENHA:", None))
        self.label_perfil.setText(QCoreApplication.translate("MainWindow", u"PERFIL:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.btn_fazer_cadastro.setText(QCoreApplication.translate("MainWindow", u"Fazer Cadastro", None))
        self.label_configuracoes.setText(QCoreApplication.translate("MainWindow", u"CONFIGURA\u00c7\u00d5ES", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Desenvolvido e publicado por:</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Keven Lucas</span></p></body></html>", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">(19) 99134-8924</span></p></body></html>", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline;\">Clique aqui para visitar o site</span></p></body></html>", None))
    # retranslateUi

