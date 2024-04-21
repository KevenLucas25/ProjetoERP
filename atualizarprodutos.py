from PySide6.QtWidgets import (
    QApplication, QDialog, QPushButton,
    QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QCheckBox
)
from database import DataBase
import sys 
from tabelaprodutos import TabelaProdutos

class AtualizarProduto(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.setWindowTitle("Atualizar Produto")

        # Passando date_edit de main_window para TabelaProdutos
        dialog_tabela = TabelaProdutos(self.main_window, self.main_window.dateEdit)
        
  
        # Definir layout para a janela de diálogo
        layout = QVBoxLayout()
        
        # Botão para abrir a lista de produtos
        btn_mostrar_produtos = QPushButton("Mostrar Produtos")
        btn_mostrar_produtos.clicked.connect(self.atualizar_tabela_produtos)
        layout.addWidget(btn_mostrar_produtos)
        
        # Adicionar o layout à janela de diálogo
        self.setLayout(layout)

        self.resize(300, 100)

    def atualizar_tabela_produtos(self):
        # Preencher a tabela de produtos com os dados do banco de dados
        dialog_tabela = TabelaProdutos(self.main_window, self.main_window.dateEdit)
        dialog_tabela.preencher_tabela()
        dialog_tabela.exec()

        self.close()
