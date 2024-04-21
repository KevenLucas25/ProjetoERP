import re
from PySide6.QtCore import Qt, QTimer,QDate,QBuffer,QByteArray,QIODevice
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                               QMessageBox, QPushButton, QHBoxLayout, QLineEdit, QDialog,
                               QLabel,QSizePolicy,QInputDialog,QFileDialog,QVBoxLayout,QTableWidget)
from PySide6.QtGui import QDoubleValidator, QIcon,QPalette,QColor,QPixmap   
from PySide6 import QtWidgets
from login import Login
from mane_python import Ui_MainWindow
from database import DataBase
import sys
import csv
import os
import locale
from atualizarprodutos import AtualizarProduto
from tabelaprodutos import TabelaProdutos

#*********************************************************************************************************************
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")
        print("Tipo de usuário recebido:", user)

        if user.lower() == "usuário" or user.lower() == "user":  
            self.btn_cadastro_usuario.setVisible(False)

        # Criar instância de AtualizarProduto passando uma referência à MainWindow
        self.atualizar_produto_dialog = AtualizarProduto(self)

        # Criar instância de TabelaProdutos passando uma referência à MainWindow
        self.tabela_produtos_dialog = TabelaProdutos(self, self.dateEdit)


        self.tabela_produtos = QTableWidget(self)
        
        self.produto_id = None

        self.criar_botoes_avancar_voltar()

        self.dateEdit.setDate(QDate.currentDate())
 #*********************************************************************************************************************       
        self.tabela_produtos.itemSelectionChanged.connect(self.selecionar_imagem)
        self.imagem_carregada = False 
        self.label_imagem = QLabel()
        self.label_imagem.setScaledContents(True)  # Redimensiona a imagem para o tamanho do QLabel
#*********************************************************************************************************************        
        # Crie o layout para o frame_imagem e adicione o QLabel
        layout = QVBoxLayout()
        layout.addWidget(self.label_imagem)
        self.frame_imagem.setLayout(layout)

        # Lista de páginas na ordem desejada
        self.paginas = [self.home_pag, self.page_estoque, self.pg_cadastrar_produto, 
                        self.pg_cadastro_usuario, self.pg_cliente, self.pg_configuracoes, 
                        self.pg_contato]
        self.pagina_atual_index = 0  # Índice da página atual na lista
        self.historico_paginas = []  # Lista para armazenar o histórico de páginas
#*********************************************************************************************************************
        # Configurar a página inicial
        self.Pages.setCurrentWidget(self.paginas[self.pagina_atual_index])

 #*********************************************************************************************************************
        self.frame_valor_total_produtos = QLabel(self.frame_valor_total_produtos)
        self.frame_valor_desconto = QLabel(self.frame_valor_desconto)
        self.frame_quantidade = QLabel(self.frame_quantidade)
        self.frame_valor_do_desconto = QLabel(self.frame_valor_do_desconto)
#*********************************************************************************************************************
        self.frame_valor_total_produtos.setStyleSheet("font-size: 20px; color: white; font-family: 'Arial'; font-weight: bold;")
        self.frame_valor_desconto.setStyleSheet("font-size: 20px; color: white; font-family: 'Arial'; font-weight: bold;")
        self.frame_quantidade.setStyleSheet("font-size: 20px; color: white; font-family: 'Arial'; font-weight: bold;")
        self.frame_valor_do_desconto.setStyleSheet("font-size: 20px; color: white; font-family: 'Arial'; font-weight: bold;")
#*********************************************************************************************************************
        self.produtos_pendentes = []
#*********************************************************************************************************************
        validator = QDoubleValidator()
        validator.setNotation(QDoubleValidator.StandardNotation)  
        validator.setDecimals(2)
        validator.setTop(1000000000)  
        self.txt_valor_produto.setValidator(validator)
        self.txt_unidade.setValidator(validator)
#*********************************************************************************************************************
        self.txt_valor_produto.editingFinished.connect(self.formatar_moeda)
        self.txt_unidade.editingFinished.connect(self.formatar_moeda)
#*********************************************************************************************************************
        validador = QDoubleValidator()
        validador.setNotation(QDoubleValidator.StandardNotation)  
        validador.setRange(0.00, 100.00)  
        validador.setDecimals(2)
        self.txt_desconto.setValidator(validador)
        self.txt_desconto.editingFinished.connect(self.formatar_porcentagem)
#*********************************************************************************************************************
        #*********************************************************************************************************************
        self.btn_editar.clicked.connect(self.editar_produto)
        self.btn_atualizar_produto.clicked.connect(self.atualizar_produto)
        self.btn_carregar_imagem.clicked.connect(self.carregar_imagem)
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.home_pag))
        self.btn_verificar_estoque.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_estoque))
        self.btn_clientes.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cliente))
        self.btn_cadastro_usuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_usuario))
        self.btn_configuracoes.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_configuracoes))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_fazer_cadastro.clicked.connect(self.subscribe_user)
        self.btn_cadastrar_produto.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastrar_produto))
        self.btn_ver_item.clicked.connect(lambda: self.Pages.setCurrentWidget(self.tb_base))

        self.btn_limpar_campos.clicked.connect(self.apagar_campos)
        self.btn_adicionar_produto.clicked.connect(self.adicionar_produto)
        self.btn_confirmar.clicked.connect(self.confirmar_produtos)
        #*********************************************************************************************************************
#*********************************************************************************************************************
    def criar_botoes_avancar_voltar(self):
    # Criação dos botões      
        self.btn_avancar = QPushButton()
        self.btn_avancar.setIcon(QIcon("imagens/seta_direita-removebg-preview.png"))  # Adicione o caminho do ícone de avançar
        self.btn_avancar.setToolTip("Avançar")  # Adiciona uma dica de ferramenta
        
        self.btn_retroceder = QPushButton()
        self.btn_retroceder.setIcon(QIcon("imagens/seta esquerda 2.png"))  # Adicione o caminho do ícone de retroceder
        self.btn_retroceder.setToolTip("Retroceder")  # Adiciona uma dica de ferramenta

        # Adicionando os botões à barra de ferramentas
        toolbar = self.addToolBar("")
        toolbar.addWidget(self.btn_retroceder)
        toolbar.addWidget(self.btn_avancar)

        # Conectar os botões aos slots correspondentes
        self.btn_avancar.clicked.connect(self.avancar_pagina)
        self.btn_retroceder.clicked.connect(self.retroceder_pagina)



        # Definir o estilo para os botões
        style = """
        QPushButton {
            color: rgb(255, 255, 255);
            border-radius: 3px;
            font-size: 16px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */
            border: 3px solid transparent;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(100, 180, 255), stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */
            color: black;
        }
        """
        self.btn_avancar.setStyleSheet(style)
        self.btn_retroceder.setStyleSheet(style)
#*********************************************************************************************************************
    def avancar_pagina(self):
        # Armazenar a página atual no histórico de páginas
        self.historico_paginas.append(self.pagina_atual_index)
        
        # Avançar para a próxima página na lista
        self.pagina_atual_index += 1
        if self.pagina_atual_index >= len(self.paginas):
            self.pagina_atual_index = 0  # Voltar para a primeira página se atingir o final da lista
        self.Pages.setCurrentWidget(self.paginas[self.pagina_atual_index])
#*********************************************************************************************************************
    def retroceder_pagina(self):
        if self.historico_paginas:
            # Remover a página atual do histórico de páginas
            self.historico_paginas.pop()
            
            # Verificar se há páginas no histórico
            if self.historico_paginas:
                # Retroceder para a página anterior no histórico
                self.pagina_atual_index = self.historico_paginas[-1]
            else:
                # Se não houver mais páginas no histórico, retroceder para a página anterior na lista
                self.pagina_atual_index -= 1
                if self.pagina_atual_index < 0:
                    self.pagina_atual_index = len(self.paginas) - 1
            self.Pages.setCurrentWidget(self.paginas[self.pagina_atual_index])



#*********************************************************************************************************************
# Configuração do local
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#*********************************************************************************************************************
    def formatar_moeda(self):
        sender = self.sender()
        valor = sender.text()

        if valor:
            try:
                # Converte a string para float, substituindo vírgula por ponto
                valor = valor.replace(",", ".")
                valor_float = float(valor)
            except ValueError:
                QMessageBox.warning(self, "Erro", "Valor inválido")
                return

            if valor_float < 10:
                self.mostrar_detalhes_erro()
                return

            # Formata o valor como moeda, agrupando milhares
            valor_formatado = locale.currency(valor_float, grouping=True)

            sender.setText(valor_formatado)
#*********************************************************************************************************************
    def mostrar_detalhes_erro(self):
        detalhes_msg = QMessageBox()
        detalhes_msg.setIcon(QMessageBox.Warning)
        detalhes_msg.setWindowTitle("Erro")
        detalhes_msg.setText("Não é possível incluir um valor menor que R$ 10,00.")

        ok_btn = QPushButton("OK")
        detalhes_msg.addButton(ok_btn, QMessageBox.RejectRole)

        detalhes_btn = QPushButton("Detalhes")
        detalhes_msg.addButton(detalhes_btn, QMessageBox.ActionRole)

        detalhes_msg.setDefaultButton(ok_btn)
        detalhes_msg.exec()

        if detalhes_msg.clickedButton() == detalhes_btn:
            detalhes_msg_detalhes = QMessageBox()
            detalhes_msg_detalhes.setIcon(QMessageBox.Information)
            detalhes_msg_detalhes.setWindowTitle("Detalhes do Erro")
            detalhes_msg_detalhes.setText("O valor não pode ser menor que R$ 10,00. \n Por favor adicione um valor maior que R$ 10,00")
            detalhes_msg_detalhes.exec()
#*********************************************************************************************************************
    def formatar_porcentagem(self):
        valor = self.txt_desconto.text()
        if valor:
            try:
                valor_float = float(valor)
            except ValueError:
                QMessageBox.warning(self, "Erro", "Valor inválido")
                return
            if valor_float < 5:
                self.mostrar_erro_desconto()
                return
            valor_porcentagem = valor_float / 100
            valor_formatado = "{:.2f}%".format(valor_porcentagem)
            self.txt_desconto.setText(valor_formatado)

#*********************************************************************************************************************
    def mostrar_erro_desconto(self):
        detalhes_msg = QMessageBox()
        detalhes_msg.setIcon(QMessageBox.Warning)
        detalhes_msg.setWindowTitle("Erro")
        detalhes_msg.setText("Por favor adicione um valor de desconto correto.")

        ok_btn = QPushButton("OK")
        detalhes_msg.addButton(ok_btn, QMessageBox.RejectRole)

        detalhes_btn = QPushButton("Detalhes")
        detalhes_msg.addButton(detalhes_btn, QMessageBox.ActionRole)

        detalhes_msg.setDefaultButton(ok_btn)
        detalhes_msg.exec()

        if detalhes_msg.clickedButton() == detalhes_btn:
            detalhes_msg_detalhes = QMessageBox()
            detalhes_msg_detalhes.setIcon(QMessageBox.Information)
            detalhes_msg_detalhes.setWindowTitle("Detalhes do Erro")
            detalhes_msg_detalhes.setText("O seu desconto não pode ser menor que 5%. \n Somente descontos maiores serão válidos para esta ação")
            detalhes_msg_detalhes.exec()
#*********************************************************************************************************************
    def subscribe_user(self):
        if not all([self.txt_nome.text(), self.txt_usuario.text(), self.txt_senha.text(), 
                    self.txt_confirmar_senha.text(), self.txt_endereco.text(), self.txt_cep.text(), self.txt_cpf.text(), 
                    self.txt_numero.text(), self.txt_estado.text(), self.txt_email.text()]):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("Todos os campos são obrigatórios.")
            msg.exec()
            return
        if self.txt_senha.text() != self.txt_confirmar_senha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("As senhas não são iguais")
            msg.exec()
            return
        if not self.is_valid_email(self.txt_email.text()):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Erro')
            msg.setText("Por favor, insira um e-mail correto")
            msg.exec()
            return

        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        senha = self.txt_senha.text()
        acesso = self.comboBox.currentText()
        endereco = self.txt_endereco.text()
        cep = self.txt_cep.text()
        cpf = self.txt_cpf.text()
        numero = self.txt_numero.text()
        estado = self.txt_estado.text()
        email = self.txt_email.text()

        db = DataBase()
        db.connecta()
        
        try:
            db.insert_user(nome, user, senha, acesso, endereco, cep, cpf, numero, estado, email)
            db.close_connection()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro de Usuário")
            msg.setText("Cadastro realizado com sucesso")
            msg.exec()
        except Exception as e:
            error_message = f"Erro ao cadastrar usuário: {str(e)}"
            QMessageBox.critical(None, "Erro", f"O  usuário {user} já está cadastrado no sistema")

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_confirmar_senha.setText("")
        self.txt_cpf.setText("")
        self.txt_email.setText("")
        self.txt_estado.setText("")
        self.txt_numero.setText("")
        self.txt_endereco.setText("")
        self.txt_cep.setText("")
#*********************************************************************************************************************
        
    def atualizar_valores_frames(self, valor_produto, quantidade, valor_com_desconto, valor_do_desconto):
    # Exibir os resultados nos frames correspondentes
        valor_produto_formatado = locale.currency(valor_produto / 100, grouping=True)
        valor_com_desconto_formatado = locale.currency(valor_com_desconto / 100, grouping=True)
        valor_do_desconto_formatado = locale.currency(valor_do_desconto / 100, grouping=True)

        self.frame_valor_total_produtos.setText(valor_produto_formatado)
        self.frame_valor_desconto.setText(valor_com_desconto_formatado)
        self.frame_quantidade.setText("{:.0f}".format(quantidade))
        self.frame_valor_do_desconto.setText(valor_do_desconto_formatado)

        # Configurar as geometrias dos frames
        altura = 101
        largura = 335

        # Ajuste a posição conforme necessário
        self.frame_valor_total_produtos.setGeometry(125, 45, largura, altura)
        self.frame_valor_desconto.setGeometry(115, 45, largura, altura)
        self.frame_quantidade.setGeometry(125, 50, largura, altura)  
        self.frame_valor_do_desconto.setGeometry(125, 50, largura, altura)

        # Atualizar os frames para exibir os novos valores
        self.frame_valor_total_produtos.adjustSize()
        self.frame_valor_desconto.adjustSize()
        self.frame_quantidade.adjustSize()
        self.frame_valor_do_desconto.adjustSize()
#*********************************************************************************************************************
    
    def subscribe_produto(self):
        if (not self.txt_produto.text() or 
            not self.txt_quantidade.text() or 
            not self.txt_valor_produto.text() or 
            not self.txt_unidade.text() or 
            not self.dateEdit.text() or 
            not self.txt_codigo_item.text() or 
            not self.txt_cliente.text() or 
            not self.txt_descricao_produto.text()):
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText("Todos os campos precisam ser preenchidos.")
            msg.exec()
            return None

        # Obter os valores dos campos
        valor_produto_str = self.txt_valor_produto.text().replace('R$', '').replace(',', '').strip()
        valor_produto = float(valor_produto_str) if valor_produto_str else 0

        quantidade_str = self.txt_quantidade.text().strip()
        quantidade = int(quantidade_str) if quantidade_str else 0

        desconto_str = self.txt_desconto.text().replace('%', '').strip()  # Removendo o símbolo de porcentagem
        desconto = float(desconto_str) if desconto_str else 0

        # Extrair o valor da unidade
        unidade_str = self.txt_unidade.text().replace('R$', '').replace(',', '').strip()
        unidade = float(unidade_str.split()[0]) if unidade_str else 0  # Extrair o valor numérico da unidade

        print("Unidade:", self.txt_unidade.text())
        print("Quantidade:", self.txt_quantidade.text())
        print("Desconto:", self.txt_desconto.text())

        # Calcular o valor total do produto antes do desconto
        resultado_unidade_quantidade = unidade * quantidade
        valor_desconto = resultado_unidade_quantidade * desconto 
        valor_com_desconto = resultado_unidade_quantidade - valor_desconto 

        # Imprimir o valor do desconto
        resultado_formatado = locale.currency(resultado_unidade_quantidade / 100, grouping=True)
        valor_desconto_formatado = locale.currency(valor_desconto / 100, grouping=True)
        valor_com_desconto_formatado = locale.currency(valor_com_desconto / 100, grouping=True)
        

    # Exibir os resultados
        print("Resultado da unidade X  quantidade:", resultado_formatado)
        print("Valor do desconto:", valor_desconto_formatado)
        print("Valor com desconto:", valor_com_desconto_formatado)

        # Adicionar os dados do produto aos produtos pendentes
        self.produtos_pendentes.append({
            "produto": self.txt_produto.text(),
            "quantidade": quantidade,
            "valor_produto": valor_produto,
            "unidade": self.txt_unidade.text(),
            "desconto": desconto,
            "data_compra": self.dateEdit.text(),
            "codigo_item": self.txt_codigo_item.text(),
            "cliente": self.txt_cliente.text(),
            "descricao_produto": self.txt_descricao_produto.text()
        })

    # Retorna os valores do produto apenas se a validação for bem-sucedida
        return valor_produto, quantidade, valor_com_desconto,valor_desconto
#*********************************************************************************************************************
    def adicionar_produto(self):
        # Obtém os valores do produto a partir da função subscribe_produto
        produto_info = self.subscribe_produto()
        
        if produto_info is not None:
            valor_produto, quantidade, valor_com_desconto, valor_do_desconto = produto_info
            # Atualiza os valores nos frames com os dados do produto
            self.atualizar_valores_frames(valor_produto, quantidade, valor_com_desconto, valor_do_desconto)
#*********************************************************************************************************************
    def inserir_produto_no_bd(self, produto_info):
        try:
            db = DataBase()
            db.connecta()

            # Formatando o valor_real com o símbolo "R$" e duas casas decimais
            valor_real_formatado = f"R$ {produto_info['valor_produto'] / 100:.2f}"

            # Formatando o desconto com o símbolo de porcentagem "%" e duas casas decimais
            desconto_formatado = f"{produto_info['desconto']:.2f}%"

            # Carregar a imagem e convertê-la para bytes
            imagem_bytes = None
            if self.imagem_carregada:
                pixmap = self.label_imagem.pixmap()
                byte_array = QByteArray()
                buffer = QBuffer(byte_array)
                buffer.open(QIODevice.WriteOnly)
                pixmap.save(buffer, "PNG")
                imagem_bytes = byte_array.toBase64().data().decode()

            # Inserindo os dados formatados no banco de dados, incluindo a imagem
            db.insert_product(
                produto_info["produto"],
                produto_info["quantidade"],
                valor_real_formatado,
                produto_info["unidade"],
                desconto_formatado,
                produto_info["data_compra"],
                produto_info["codigo_item"],
                produto_info["cliente"],
                produto_info["descricao_produto"],
                imagem_bytes  # Adicionando a imagem aqui
            )
            db.close_connection()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar produto: {str(e)}")

#*******************************************************************************************************
    def conectar_botao_adicionar_produto(self):
        self.btn_adicionar_produto.clicked.connect(self.adicionar_produto)
#***************************************************************************************************************
    def confirmar_produtos(self):
    # Verificar se há produtos pendentes para confirmar
        if not self.produtos_pendentes:
            QMessageBox.warning(self, "Aviso", "Não há produtos pendentes para confirmar.")
            return

        # Verificar se todos os campos obrigatórios estão preenchidos
        if not self.campos_obrigatorios_preenchidos():
            return

        # Verificar se a imagem está carregada
        if not self.imagem_carregada:
            # Perguntar ao usuário se ele deseja seguir sem uma imagem
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText("O produto não contém imagem. Deseja confirmar mesmo assim?")
            msgBox.setWindowTitle("Aviso")
            
            # Definindo os botões em português
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setButtonText(QMessageBox.Yes, "Sim")
            msgBox.setButtonText(QMessageBox.No, "Não")

            resposta = msgBox.exec()

            if resposta == QMessageBox.No:
                return

        # Salvar os produtos pendentes no banco de dados
        for produto in self.produtos_pendentes:
            self.inserir_produto_no_bd(produto)

        # Limpar a lista de produtos pendentes
        self.produtos_pendentes.clear()

        # Limpar os campos de entrada
        self.limpar_campos()
        
        # Limpar a imagem
        self.label_imagem.clear()

        self.dateEdit.setDate(QDate.currentDate())  # Define a data atual
        self.dateEdit.clear()

        # Exibir mensagem de sucesso apenas se todos os campos estiverem preenchidos
        self.mostrar_mensagem_sucesso()

        self.limpar_frames()
#***************************************************************************************************************
    def limpar_frames(self):
        self.frame_valor_total_produtos.clear()
        self.frame_valor_desconto.clear()
        self.frame_quantidade.clear()
        self.frame_valor_do_desconto.clear() 
#***************************************************************************************************************
    def carregar_imagem(self):
    # Abre uma janela de diálogo para selecionar a imagem do produto
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Selecionar Imagem")
        file_dialog.setNameFilter("Imagens (*.png *.jpg *.jpeg *.bmp *.gif)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        
        # Verifica se o usuário selecionou um arquivo
        if file_dialog.exec():
            # Obtém o caminho do arquivo selecionado
            file_path = file_dialog.selectedFiles()[0]
            
            # Carrega a nova imagem no QLabel
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                self.label_imagem.setPixmap(pixmap)
                self.imagem_carregada = True 
            else:
                print("Erro ao carregar a imagem:", file_path)  # Mensagem de depuração 
#*********************************************************************************************************************
    def editar_produto(self):
    # Criar uma instância da janela de atualização de produto
        dialog_atualizacao = AtualizarProduto(self)
        
        # Exibir a janela de atualização de produto
        dialog_atualizacao.exec()
#*********************************************************************************************************************
    def selecionar_imagem(self, row):
    # Obter o ID do produto selecionado
        produto_id = self.tabela_produtos.item(row, 0).text()
        self.produto_id = produto_id
        
        # Atualizar os campos e a imagem com base no produto selecionado
        self.atualizar_campos()
        self.atualizar_imagem()
#*********************************************************************************************************************
    def atualizar_produto(self):
    # Verificar se algum produto foi selecionado na tabela
        if not self.produto_id:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Não há produto selecionado para seguir.")
            msgBox.setWindowTitle("Aviso")
            
            # Adicionar botão "Detalhes"
            detalhes_button = msgBox.addButton("Detalhes", QMessageBox.ActionRole)
            msgBox.addButton(QMessageBox.Ok)
            
            clicked_button = msgBox.exec()
            
            if clicked_button == QMessageBox.Ok:
                return
            elif msgBox.clickedButton() == detalhes_button:
                # Criar uma caixa de mensagem de informação com o estilo personalizado
                detalhesMsgBox = QMessageBox()
                detalhesMsgBox.setIcon(QMessageBox.Information)
                detalhesMsgBox.setText("É necessário primeiro inserir um produto, através do botão  EDITAR.")
                detalhesMsgBox.setWindowTitle("Detalhes")
                
                detalhesMsgBox.exec()
                
                return
        else:
            self.atualizar_imagem()
  
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
            produto_id = self.produto_id  # Obter o ID do produto definido pela TabelaProdutos
            produto_imagem = self.produto_imagem

            # Conectar ao banco de dados
            db = DataBase()
            try:
                db.connecta()
                # Atualizar o produto no banco de dados
                db.atualizar_produto(produto_id, produto_nome, produto_quantidade, produto_valor_real,
                                    produto_unidade, produto_desconto, produto_data_compra, 
                                    produto_codigo_item, produto_cliente, produto_descricao,produto_imagem)
                QMessageBox.information(self, "Sucesso", "Produto atualizado com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao atualizar o produto: {str(e)}")
            finally:
                # Fechar a conexão com o banco de dados
                db.close_connection()

#*******************************************************************************************************
    def atualizar_imagem(self):
            caminho_imagem = self.obter_caminho_imagem(self.produto_id)
            if caminho_imagem:
                # Carregar a imagem e exibi-la em um QLabel
                pixmap = QPixmap(caminho_imagem)
                if not pixmap.isNull():
                    # Redimensionar a imagem para se ajustar ao QLabel (se necessário)
                    pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
                    
                    self.label_imagem.setPixmap(pixmap)
                else:
                    QMessageBox.warning(self, "Aviso", "Não foi possível carregar a imagem.")
            else:
                QMessageBox.warning(self, "Aviso", "Não foi possível encontrar o caminho da imagem.")
#*******************************************************************************************************
    def mostrar_erro_desconto(self):
        detalhes_msg_detalhes = QMessageBox()
        detalhes_msg_detalhes.setIcon(QMessageBox.Information)
        detalhes_msg_detalhes.setWindowTitle("Detalhes do Erro")
        detalhes_msg_detalhes.setText("Os campos obrigatórios precisam estar preenchidos.")
        detalhes_msg_detalhes.exec()
#*******************************************************************************************************
    def campos_obrigatorios_preenchidos(self):
        # Verifique aqui se todos os campos obrigatórios estão preenchidos
        # Se estiverem preenchidos, retorne True, caso contrário, exiba uma mensagem de erro e retorne False
        # Por exemplo:
        if not all([self.txt_produto.text(), self.txt_quantidade.text(), self.txt_valor_produto.text(),
                    self.txt_unidade.text(), self.dateEdit.text(), self.txt_codigo_item.text(),
                    self.txt_cliente.text(), self.txt_descricao_produto.text()]):
            QMessageBox.warning(self, "Aviso", "Todos os campos obrigatórios devem ser preenchidos.")
            return False
        return True
#*******************************************************************************************************
    def mostrar_mensagem_sucesso(self):
        success_msg = QMessageBox()
        success_msg.setIcon(QMessageBox.Information)
        success_msg.setWindowTitle("Sucesso")
        success_msg.setText("Produtos confirmados e cadastrados com sucesso.")
        # Definindo o estilo para tornar o texto preto
        success_msg.setStyleSheet("color: black;")
        success_msg.exec()
#*******************************************************************************************************
    def limpar_campos(self):
        self.txt_produto.clear()
        self.txt_quantidade.clear()
        self.txt_valor_produto.clear()
        self.txt_unidade.clear()
        self.txt_desconto.clear()
        self.dateEdit.clear()
        self.txt_codigo_item.clear()
        self.txt_cliente.clear()
        self.txt_descricao_produto.clear()
#*******************************************************************************************************
    def apagar_campos(self):
    # Criar uma caixa de mensagem com o botão DETALHES
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Não há campos preenchidos para limpar.")
        msgBox.setWindowTitle("Aviso")
          
        # Verificar se algum campo já está vazio
        if not any([
            self.txt_produto.text(),
            self.txt_quantidade.text(),
            self.txt_valor_produto.text(),
            self.txt_unidade.text(),
            self.txt_desconto.text(),
            self.txt_codigo_item.text(),
            self.txt_cliente.text(),
            self.txt_descricao_produto.text()
        ]):
            # Adicionar o botão DETALHES
            detalhes_button = msgBox.addButton("Detalhes", QMessageBox.ActionRole)
            
            # Adicionar os outros botões padrão (Ok)
            msgBox.setStandardButtons(QMessageBox.Ok)

            returnValue = msgBox.exec()
            
            if returnValue == QMessageBox.Ok:
                return
            elif msgBox.clickedButton() == detalhes_button:
            # Criar uma caixa de mensagem de informação com o estilo personalizado
                detalhesMsgBox = QMessageBox()
                detalhesMsgBox.setIcon(QMessageBox.Information)
                detalhesMsgBox.setText("É necessário atualizar um produto para seguir com essa ação.")
                detalhesMsgBox.setWindowTitle("Detalhes")
                
                # Definir o estilo da QMessageBox
                detalhesMsgBox.setStyleSheet("QMessageBox { background-color: white; } "
                                            "QMessageBox QLabel { color: black; }")
                
                detalhesMsgBox.exec()
        
        # Limpar todos os campos das QLineEdit
        self.txt_produto.clear()
        self.txt_quantidade.clear()
        self.txt_valor_produto.clear()
        self.txt_unidade.clear()
        self.txt_desconto.clear()
        self.txt_codigo_item.clear()
        self.txt_cliente.clear()
        self.txt_descricao_produto.clear()

        self.limpar_imagem()

        # Limpar o campo dateEdit e configurar para a data atual
        self.dateEdit.setDate(QDate.currentDate())
#***************************************************************************************************************
    def limpar_imagem(self):
        # Verificar se o QFrame contém um QLabel para imagem
        for widget in self.frame_imagem.children():
            if isinstance(widget, QLabel):
                widget.clear()  # Limpar o QLabel
                widget.setPixmap(QPixmap())  # Definir um pixmap vazio ou padrão

        successMsgBox = QMessageBox()
        successMsgBox.setIcon(QMessageBox.Information)
        successMsgBox.setText("Campos limpos com sucesso!")
        successMsgBox.setWindowTitle("Sucesso")

        successMsgBox.exec()

#*******************************************************************************************************
    def is_valid_email(self, email):
        email = email.strip()
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3,}$')
        return bool(email_pattern.match(email))
# **********************************************************************************************************************
    def configurar_geometria_frames(self):
        altura = 101
        largura = 335
        self.frame_valor_total_produtos.setGeometry(335, 101, largura, altura)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())
