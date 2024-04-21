from PySide6.QtWidgets import (QDialog, QPushButton, QVBoxLayout, QTableWidget, 
                               QTableWidgetItem, QMessageBox, QCheckBox, QLabel, QLineEdit, 
                               QLabel, QFrame,QDateEdit,QGridLayout)
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, Qt, QImage
from PySide6.QtCore import QDate, Qt
from database import DataBase, sqlite3
import base64
import re
class TabelaProdutos(QDialog):
    def __init__(self, main_window, date_edit, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.date_edit = date_edit
        self.db = DataBase()  # Inicializando o atributo db
        self.setWindowTitle("Tabela de Produtos")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.frame_valor_total_produtos = QtWidgets.QFrame()
        self.frame_valor_do_desconto = QtWidgets.QFrame()
        self.frame_valor_desconto = QtWidgets.QFrame()
        self.frame_quantidade = QtWidgets.QFrame()


        cursor = None
        
        # Layout principal da janela
        layout = QVBoxLayout()

        self.grid_layout = QGridLayout()

        #layout.addLayout(self.grid_layout)
        #layout.addWidget(self.table_widget)


        # Defina o layout para o diálogo
        #self.setLayout(layout)
        
        

        # Tabela para exibir os produtos
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(11)  # Definindo o número de colunas
        self.table_widget.setHorizontalHeaderLabels(["ID", "Produto", "Quantidade", "Valor Real do Produto", 
                                                     "Valor da Unidade", "Desconto", "Data da Compra", "Código do Produto", 
                                                     "Cliente", "Descrição", "Imagem"])  # Definindo os rótulos das colunas
        
        # Personalizar o estilo dos cabeçalhos de linha e coluna
        font = self.table_widget.horizontalHeader().font()
        font.setBold(True)
        self.table_widget.horizontalHeader().setFont(font)
        self.table_widget.verticalHeader().setFont(font)

        # Botão para apagar produto, dentro da tabela produtos
        self.btn_apagar_produto = QPushButton("Apagar Produto")
        layout.addWidget(self.btn_apagar_produto)

        self.btn_editar_produto = QPushButton("Atualizar Produto")
        layout.addWidget(self.btn_editar_produto)

        self.btn_filtrar_produtos = QPushButton("Filtrar Produtos")
        layout.addWidget(self.btn_filtrar_produtos)

        self.btn_selecionar_todos = QCheckBox("Selecionar Produtos")
        layout.addWidget(self.btn_selecionar_todos)
        
        self.btn_ordenar_produtos = QPushButton("Ordenar Produtos")
        layout.addWidget(self.btn_ordenar_produtos)

        self.btn_visualizar_imagem = QPushButton("Visualizar Imagem")
        layout.addWidget(self.btn_visualizar_imagem)

        # Adicionar a tabela ao layout
        layout.addWidget(self.table_widget)
        
        # Definir o layout da janela
        self.setLayout(layout)
 

        self.btn_apagar_produto.clicked.connect(self.confirmar_apagar_produto)
        self.btn_editar_produto.clicked.connect(self.editar_produto)
        self.btn_filtrar_produtos.clicked.connect(self.filtrar_produtos)
        self.btn_ordenar_produtos.clicked.connect(self.ordenar_produtos)
        self.btn_visualizar_imagem.clicked.connect(self.visualizar_imagem)
        self.btn_selecionar_todos.clicked.connect(self.selecionar_todos)
        self.btn_filtrar_produtos.clicked.connect(self.filtrar_produtos)
        self.btn_ordenar_produtos.clicked.connect(self.ordenar_produtos)
    
#*******************************************************************************************************
    def preencher_tabela(self):
    # Limpar a tabela antes de preencher
        self.table_widget.setRowCount(0)
        
        # Conectar ao banco de dados
        db = DataBase()
        try:
            db.connecta()
            
            # Obter os produtos do banco de dados
            produtos = db.get_products()
            
            # Preencher a tabela com os dados dos produtos
            for produto in produtos:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)
                for col, data in enumerate(produto):
                    item = QTableWidgetItem(str(data))
                    self.table_widget.setItem(row_position, col, item)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao acessar o banco de dados: {str(e)}")
        finally:
            # Fechar a conexão com o banco de dados
            db.close_connection()
        
#*******************************************************************************************************
    def confirmar_apagar_produto(self):
        # Verificar se uma linha está selecionada
        if self.table_widget.currentRow() >= 0:
            # Exibir uma mensagem de confirmação
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Confirmar")
            msg_box.setText("Você tem certeza que deseja apagar este produto?")
            
            sim_button = QPushButton("Sim")
            sim_button.clicked.connect(self.apagar_produto_confirmado)
            msg_box.addButton(sim_button, QMessageBox.YesRole)
            
            nao_button = QPushButton("Não")
            nao_button.clicked.connect(msg_box.reject)
            msg_box.addButton(nao_button, QMessageBox.NoRole)

            # Exibir a caixa de mensagem
            msg_box.exec()
        else:
            QMessageBox.warning(self, "Aviso", "Nenhum produto selecionado.")
#*******************************************************************************************************    
    def apagar_produto_confirmado(self):
        # Obter o índice da linha selecionada
        index = self.table_widget.currentRow()
        # Obter o ID do produto da coluna 0 (ID)
        produto_id = int(self.table_widget.item(index, 0).text())
        # Remover a linha da tabela
        self.table_widget.removeRow(index)
        # Remover o produto do banco de dados
        db = DataBase()
        try:
            db.connecta()
            db.remover_produto(produto_id)
            QMessageBox.information(self, "Sucesso", "Produto removido com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao remover o produto: {str(e)}")
        finally:
            # Fechar a conexão com o banco de dados
            db.close_connection()

#*******************************************************************************************************
    def recuperar_imagem_do_banco(self, produto_id):
        imagem_blob = None
        
        try:
            connection = self.db.connecta()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT Imagem FROM products WHERE id = ?", (produto_id,))
                result = cursor.fetchone()

                if result:
                    imagem_blob = result[0]
                else:
                    print(f"Imagem não encontrada para o produto: {produto_id}")
                    return None

        except Exception as e:
            print(f"Erro ao recuperar imagem do banco de dados: {str(e)}")
            return None

        finally:
            self.db.close_connection()

        if imagem_blob:
            try:
                imagem_data = base64.b64decode(imagem_blob)
                return imagem_data  # Retorna bytes decodificados
                
            except Exception as e:
                print(f"Erro ao decodificar imagem: {str(e)}")
                return None
        else:
            print("Imagem não encontrada para o produto:", produto_id)
            return None
#*******************************************************************************************************
    def editar_produto(self):
        if self.table_widget.currentRow() >= 0:
            row_index = self.table_widget.currentRow()
            produto_id = int(self.table_widget.item(row_index, 0).text())
            
            imagem_data = self.recuperar_imagem_do_banco(produto_id)

            # Limpe os widgets anteriores do grid_layout
            while self.grid_layout.count():
                item = self.grid_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

            
            # Obter os dados do produto selecionado
            produto_nome = self.table_widget.item(row_index, 1).text()
            produto_quantidade = self.table_widget.item(row_index, 2).text()
            produto_valor_real = self.table_widget.item(row_index, 3).text()
            produto_unidade = self.table_widget.item(row_index, 4).text()
            produto_desconto = self.table_widget.item(row_index, 5).text()
            produto_dateEdit = self.table_widget.item(row_index, 6).text()
            produto_codigo_item = self.table_widget.item(row_index, 7).text()
            produto_cliente = self.table_widget.item(row_index, 8).text()
            produto_descricao = self.table_widget.item(row_index, 9).text()
            
            # Preencher os campos da MainWindow com os dados do produto selecionado
            self.main_window.txt_produto.setText(produto_nome)
            self.main_window.txt_quantidade.setText(produto_quantidade)
            self.main_window.txt_valor_produto.setText(produto_valor_real)
            self.main_window.txt_unidade.setText(produto_unidade)
            self.main_window.txt_desconto.setText(produto_desconto)
            self.date_edit.setDate(QDate.fromString(produto_dateEdit, "dd/MM/yyyy"))
            self.main_window.txt_codigo_item.setText(produto_codigo_item)
            self.main_window.txt_cliente.setText(produto_cliente)
            self.main_window.txt_descricao_produto.setText(produto_descricao)

            produto_quantidade = float(produto_quantidade)
            produto_valor_real = float(re.sub(r'[^\d.]', '', produto_valor_real)) / 100  # Remove caracteres não numéricos e divide por 100 para converter centavos para reais
            produto_desconto = float(re.sub(r'[^\d.]', '', produto_desconto)) / 100  # Remove caracteres não numéricos e divide por 100 para converter percentual para decimal

            # Calcular os valores
            valor_total = produto_valor_real * produto_quantidade
            valor_com_desconto = produto_valor_real - (produto_valor_real * produto_desconto)
            valor_do_desconto = produto_valor_real * produto_desconto

            # Atualizar os frames com os valores calculados
            self.main_window.frame_valor_total_produtos.setText(f"R$ {valor_total:.2f}")
            self.main_window.frame_valor_desconto.setText(f"R$ {valor_do_desconto:.2f}")
            self.main_window.frame_quantidade.setText(str(produto_quantidade))
            self.main_window.frame_valor_do_desconto.setText(f"R$ {valor_com_desconto:.2f}")

            # Definir as dimensões dos frames
            largura = 335
            altura = 101
            self.main_window.frame_valor_total_produtos.setGeometry(125, 28, largura, altura)
            self.main_window.frame_valor_desconto.setGeometry(115, 28, largura, altura)
            self.main_window.frame_quantidade.setGeometry(125, 28, largura, altura)
            self.main_window.frame_valor_do_desconto.setGeometry(125, 25, largura, altura)


            # Definir o tamanho máximo para o texto nos labels dos frames
            self.main_window.frame_valor_total_produtos.setMaximumWidth(largura)    
            self.main_window.frame_valor_desconto.setMaximumWidth(largura)
            self.main_window.frame_quantidade.setMaximumWidth(largura)
            self.main_window.frame_valor_do_desconto.setMaximumWidth(largura)


            if imagem_data:
                try:
                    pixmap = QPixmap()
                    pixmap.loadFromData(imagem_data)
                    
                    if pixmap.isNull():
                        print("Aviso: pixmap é nulo")
                        QMessageBox.warning(self, "Aviso", "Não foi possível carregar a imagem.")
                        return
                    else:
                        print("Pixmap carregado com sucesso.")

                    # Criar um QLabel para exibir a imagem
                    label_imagem = QLabel(self.main_window.frame_imagem)
                    
                    # Definir tamanho do QLabel para ser o mesmo que o QFrame
                    frame_size = self.main_window.frame_imagem.size()
                    label_imagem.setFixedSize(frame_size.width(), frame_size.height())
                    
                    # Redimensionar o pixmap para se ajustar ao QLabel
                    pixmap = pixmap.scaled(label_imagem.width(), label_imagem.height(), Qt.KeepAspectRatio)
                    
                    label_imagem.setPixmap(pixmap)
                    
                    # Ajustar o alinhamento da imagem no QLabel
                    label_imagem.setAlignment(Qt.AlignCenter)
                                      
                    # Mostrar o QLabel
                    label_imagem.show()
                    
                    # Atualizar o QLabel
                    label_imagem.repaint()

                except Exception as e:
                    print(f"Erro ao processar imagem: {str(e)}")
            else:
                print("Imagem não encontrada no banco de dados.")
                # Limpar a frame_imagem
                if self.main_window.frame_imagem.layout():
                    old_layout = self.main_window.frame_imagem.layout()
                    while old_layout.count():
                        item = old_layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.deleteLater()
                    self.main_window.frame_imagem.setLayout(None)

#*******************************************************************************************************

    def adicionar_widgets(self, frame, debug_text):
        layout = QVBoxLayout()  # Criar um layout vertical
        label = QLabel(debug_text)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)  # Adicionar o label ao layout
        frame.setLayout(layout)  # Definir o layout ao frame
#*******************************************************************************************************     
    def atualizar_produto(self):
    # Obter os dados dos campos
        produto_nome = self.txt_produto.text()
        produto_quantidade = self.txt_quantidade.text()
        produto_valor_real = self.txt_valor_produto.text()
        produto_unidade = self.txt_unidade.text()
        produto_desconto = self.txt_desconto.text()
        produto_data_compra = self.dateEdit.date().toString("dd/MM/yyyy")
        produto_codigo_item = self.txt_codigo_item.text()
        produto_cliente = self.txt_cliente.text()
        produto_descricao = self.txt_descricao_produto.text()
        
        # Verificar se há uma imagem definida
        if self.main_window.frame_imagem.pixmap() is not None:
            produto_imagem = self.main_window.frame_imagem.pixmap().toImage()
        else:
            produto_imagem = None
        
        produto_id = self.produto_id  # Obter o ID do produto definido pela TabelaProdutos

        # Conectar ao banco de dados
        db = DataBase()
        try:
            self.db.connecta()
            
            # Atualizar o produto no banco de dados
            db.atualizar_produto(produto_id, produto_nome, produto_quantidade, produto_valor_real,
                                produto_unidade, produto_desconto, produto_data_compra, 
                                produto_codigo_item, produto_cliente, produto_descricao, 
                                produto_imagem)  # Incluindo a imagem no método de atualização
            
            QMessageBox.information(self, "Sucesso", "Produto atualizado com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao atualizar o produto: {str(e)}")
        finally:
            # Fechar a conexão com o banco de dados
            self.db.close_connection()


    #*******************************************************************************************************
    def atualizar_tabela_produtos_filtrada(self, produtos):
    # Limpar a tabela antes de preencher com os produtos filtrados
        self.table_widget.setRowCount(0)

        # Preencher a tabela com os produtos filtrados
        for produto in produtos:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            for col, data in enumerate(produto):
                item = QTableWidgetItem(str(data))
                self.table_widget.setItem(row_position, col, item)

#*******************************************************************************************************
    def obter_produtos_por_nome(self, nome):
        query = "SELECT * FROM products WHERE Produto LIKE ?"
        parameters = (f"%{nome}%",)  # Usamos LIKE com % para fazer a consulta parcial

        cursor = None  # Inicialize o cursor como None
        
        try:
            db = DataBase()  # Cria uma instância da classe DataBase
            connection = db.connecta()  # Obtemos uma conexão
            cursor = connection.cursor()  # Criamos um cursor a partir da conexão
            cursor.execute(query, parameters)
            
            produtos = cursor.fetchall()
            
            return produtos
        except Exception as e:
            print("Erro ao consultar produtos:", e)
            return []
        finally:
            if cursor:
                cursor.close()  # Fechamos o cursor apenas se ele não for None
            db.close_connection()  # Fechamos a conexão usando a instância de DataBase

#*******************************************************************************************************
    def filtrar_produtos(self):
    # Perguntar ao usuário se ele deseja filtrar os produtos
        filtro = QMessageBox.question(self, "Filtrar Produtos", "Deseja filtrar os produtos?", QMessageBox.Yes | QMessageBox.No)
        
        if filtro == QMessageBox.Yes:
            dialog = QDialog(self)
            dialog.setWindowTitle("Filtrar por Nome")
            
            layout = QVBoxLayout()
            
            # Label e campo de entrada para o nome do produto
            lbl_nome = QLabel("Nome do Produto:")
            txt_nome = QLineEdit()
            layout.addWidget(lbl_nome)
            layout.addWidget(txt_nome)
            
            # Botão para aplicar o filtro
            btn_filtrar = QPushButton("Filtrar")
            
            def aplicar_filtro():
                nome = txt_nome.text()
                print(f"Filtrando por Nome: {nome}")
                
                produtos = self.obter_produtos_por_nome(nome)
                self.atualizar_tabela_produtos_filtrada(produtos)
                
                dialog.close()
            
            btn_filtrar.clicked.connect(aplicar_filtro)
            layout.addWidget(btn_filtrar)
            
            dialog.setLayout(layout)
            dialog.exec_()
        else:
            return

#*******************************************************************************************************
    def selecionar_todos(self):
        # Implementação para selecionar todos os produtos na tabela
        total_rows = self.table_widget.rowCount()
        for row in range(total_rows):
            item = self.table_widget.item(row, 0)  # Assumindo que o ID está na coluna 0
            item.setSelected(True)
#*******************************************************************************************************
    def ordenar_produtos(self):
        # Implementação básica para ordenar produtos
        self.table_widget.sortItems(1, Qt.AscendingOrder)  # Ordenar pela coluna 1 em ordem ascendente
#*******************************************************************************************************
    def visualizar_imagem(self):
        if self.table_widget.currentRow() >= 0:
            row_index = self.table_widget.currentRow()
            produto_id = int(self.table_widget.item(row_index, 0).text())
            
            imagem_data = self.recuperar_imagem_do_banco(produto_id)
            
            if imagem_data:
                try:
                    print("Dados da imagem recuperados com sucesso para visualização.")
                    
                    pixmap = QPixmap()
                    pixmap.loadFromData(imagem_data)
                    
                    if pixmap.isNull():
                        print("Aviso: pixmap é nulo")
                        QMessageBox.warning(self, "Aviso", "Não foi possível carregar a imagem.")
                        return
                    else:
                        print("Pixmap carregado com sucesso para visualização.")
                    
                    visualizar_janela = QDialog(self)
                    visualizar_janela.setWindowTitle("Visualizar Imagem")
                    visualizar_janela.setMinimumSize(400, 400)
                    
                    label_imagem = QLabel(visualizar_janela)
                    label_imagem.setPixmap(pixmap.scaled(label_imagem.width(), label_imagem.height(), Qt.KeepAspectRatio))
                    
                    layout = QVBoxLayout()
                    layout.addWidget(label_imagem)
                    visualizar_janela.setLayout(layout)
                    
                    visualizar_janela.exec()
                    
                except Exception as e:
                    print(f"Erro ao processar imagem: {str(e)}")
            else:
                QMessageBox.warning(self, "Aviso", "Imagem não encontrada.")



#*******************************************************************************************************
    def verificar_usuario(self, usuario, senha):
        # Consulta SQL para verificar o usuário e senha
        query = "SELECT Acesso FROM users WHERE Usuário = ? AND Senha = ? COLLATE NOCASE"
        parameters = (usuario, senha)

        cursor = None  # Inicialize o cursor como None
        
        try:
            # Obter o cursor usando o método da classe DataBase
            cursor = self.db.execute_query(query, parameters)
            
            resultado = cursor.fetchone()
            
            if resultado:
                tipo_usuario = resultado[0]
                print(f"Resultado da consulta: {resultado}")
                print("Usuário autenticado com sucesso")
                return tipo_usuario.lower()
            else:
                print("Usuário ou senha incorretos")
                return None
        except Exception as e:
            print(f"Erro ao verificar usuário: {str(e)}")
            return None
        finally:
            # Fechar o cursor se ele foi inicializado
            if cursor:
                cursor.close()
#*******************************************************************************************************
    def obter_produtos_por_nome(self, nome):
        query = "SELECT * FROM products WHERE Produto LIKE ?"
        parameters = (f"%{nome}%",)  # Usamos LIKE com % para fazer a consulta parcial

        cursor = None  # Inicialize o cursor como None
        
        try:
            db = DataBase()  # Cria uma instância da classe DataBase
            connection = db.connecta()  # Obtemos uma conexão
            cursor = connection.cursor()  # Criamos um cursor a partir da conexão
            cursor.execute(query, parameters)
            
            produtos = cursor.fetchall()
            
            return produtos
        except Exception as e:
            print("Erro ao consultar produtos:", e)
            return []
        finally:
            if cursor:
                cursor.close()  # Fechamos o cursor apenas se ele não for None
            db.close_connection()  # Fechamos a conexão usando a instância de DataBase