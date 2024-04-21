import sqlite3

class DataBase:
    def __init__(self, name="banco_de_dados.db"):
        self.name = name
        self.connection = None
    
    def connecta(self):
        try:
            self.connection = sqlite3.connect(self.name)
            return self.connection
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {str(e)}")
            return None

    
    def close_connection(self):
        try:
            if self.connection:  # Verificar se a conexão existe antes de fechar
                self.connection.close()
        except Exception as e:
            print("Erro ao fechar conexão:", e)

    
    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Nome TEXT NOT NULL,
                    Usuário TEXT UNIQUE NOT NULL,
                    Senha TEXT NOT NULL,
                    Acesso TEXT NOT NULL,
                    Endereço TEXT,
                    CEP TEXT,
                    CPF TEXT,
                    Número TEXT,
                    Estado TEXT,
                    Email TEXT
                )
            """)
        except Exception as e:
            print("Erro ao criar tabela de usuários:", e)

    def create_table_products(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Produto TEXT NOT NULL,
                    Quantidade INTEGER NOT NULL,
                    Valor_Real REAL NOT NULL,
                    Valor_Unidade REAL NOT NULL,
                    Desconto REAL,
                    Data_Compra TEXT,
                    Código_Item TEXT,
                    Cliente TEXT,
                    Descrição_Produto TEXT            
                )
            """)
            print("Tabela de produtos criada com sucesso!")
        except Exception as e:
            print("Erro ao criar tabela de produtos:", e)


    def insert_product(self, produto, quantidade, valor_real, valor_unidade, desconto, data_compra, codigo_item, cliente, descricao_produto, imagem=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO products(Produto, Quantidade, Valor_Real, Valor_Unidade, Desconto, Data_Compra, Código_Item, Cliente, Descrição_Produto, Imagem) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (produto, quantidade, valor_real, valor_unidade, desconto, data_compra, codigo_item, cliente, descricao_produto, imagem))
            self.connection.commit()
            print("Produto inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir produto:", e)

    def insert_image(self, produto_id, imagem):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE products
                SET Imagem = ?
                WHERE id = ?
            """, (imagem, produto_id))
            self.connection.commit()
            print("Imagem inserida com sucesso!")
        except Exception as e:
            print("Erro ao inserir imagem:", e)
#*********************************************************************************************************************
    def retrieve_image(self, produto_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT Imagem FROM products WHERE id = ?", (produto_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            print("Erro ao recuperar imagem:", e)
            return None
#*********************************************************************************************************************
    def check_user(self, usuario, senha):
        try:
            print("Verificando usuário e senha no banco de dados...")
            print("Usuário fornecido:", usuario)
            print("Senha fornecida:", senha)
            
            query = "SELECT Acesso FROM users WHERE Usuário = ? AND Senha = ? COLLATE NOCASE"  # Comparação insensível a maiúsculas e minúsculas
            cursor = self.connection.cursor()
            cursor.execute(query, (usuario, senha))
            result = cursor.fetchone()
            print("Resultado da consulta:", result)
            if result:
                print("Usuário autenticado com sucesso")
                return result[0]  # Retorna o tipo de usuário
            else:
                return ""  # Retorna uma string vazia se as credenciais não corresponderem
        except Exception as e:
            print("Erro ao verificar usuário:", e)
            return ""
    #*********************************************************************************************************************
    def user_exists(self, usuario):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT 1 FROM users WHERE Usuário = ?", (usuario,))
            result = cursor.fetchone()
            return bool(result)  # Retorna True se o usuário existir, False caso contrário
        except Exception as e:
            print("Erro ao verificar se usuário existe:", e)
            return False
        
   #*********************************************************************************************************************

    def get_products(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM products")
            produtos = cursor.fetchall()
            return produtos
        except Exception as e:
            print("Erro ao obter produtos:", e)
            return []
 #*********************************************************************************************************************       
    def remover_produto(self, produto_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM products WHERE id = ?", (produto_id,))
            self.connection.commit()
            print("Produto removido com sucesso!")
        except Exception as e:
            print("Erro ao apagar produto do banco de dados:", e)
#*********************************************************************************************************************
    def atualizar_produto(self, produto_id, produto=None, quantidade=None, 
                          valor_real=None, valor_unidade=None, desconto=None, 
                          data_compra=None, codigo_item=None, cliente=None, descricao_produto=None,produto_imagem=None):
        try:
            # Monta a query SQL dinamicamente com base nos parâmetros fornecidos
            columns_to_update = []
            values_to_update = []
            
            if produto:
                columns_to_update.append("Produto = ?")
                values_to_update.append(produto)
            if quantidade is not None:
                columns_to_update.append("Quantidade = ?")
                values_to_update.append(quantidade)
            if valor_real is not None:
                columns_to_update.append("Valor_Real = ?")
                values_to_update.append(valor_real)
            if valor_unidade is not None:
                columns_to_update.append("Valor_Unidade = ?")
                values_to_update.append(valor_unidade)
            if desconto is not None:
                columns_to_update.append("Desconto = ?")
                values_to_update.append(desconto)
            if data_compra:
                columns_to_update.append("Data_Compra = ?")
                values_to_update.append(data_compra)
            if codigo_item:
                columns_to_update.append("Código_Item = ?")
                values_to_update.append(codigo_item)
            if cliente:
                columns_to_update.append("Cliente = ?")
                values_to_update.append(cliente)
            if descricao_produto:
                columns_to_update.append("Descrição_Produto = ?")
                values_to_update.append(descricao_produto)
            if produto_imagem:
                columns_to_update.append("Imagem")
                values_to_update.append(produto_imagem)
            
            # Converte as listas em strings separadas por vírgula
            set_clause = ", ".join(columns_to_update)
            
            query = f"""
                UPDATE products
                SET {set_clause}
                WHERE id = ?
            """
            
            # Adiciona o produto_id ao final da lista de valores
            values_to_update.append(produto_id)
            
            cursor = self.connection.cursor()
            cursor.execute(query, tuple(values_to_update))
            self.connection.commit()
            
            print("Produto atualizado com sucesso!")
        except Exception as e:
            print("Erro ao atualizar produto:", e)

    def obter_caminho_imagem(self, produto_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT Imagem FROM products WHERE id = ?", (produto_id,))
            resultado = cursor.fetchone()
            
            if resultado:
                # Retorna o caminho da imagem se o produto for encontrado
                return resultado[0]
            else:
                # Retorna None se o produto não for encontrado
                return None
        except Exception as e:
            print("Erro ao obter caminho da imagem:", e)
            return None



if __name__ == "__main__":
    db = DataBase()
    db.connecta()
    db.close_connection()
    db.add_column_imagem()
