import pyodbc
import customtkinter

# Configuração da aparência
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Criação da janela principal
app = customtkinter.CTk()
app.geometry("400x600")
app.title("CRIAR E CONECTAR MS AO BANCO DE DADOS")

# Campo de entrada para o nome do banco de dados
entry_database = customtkinter.CTkEntry(app, placeholder_text="Nome do Banco de Dados")
entry_database.place(relx=0.3, rely=0.3)

# Função para criar o banco de dados
def create_db():
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'Server=LAPTOP-VNB6KU8U\\SQLEXPRESS;'
            'DATABASE=master;'  # Correção: Uso de 'DATABASE' e 'master'
            'Trusted_Connection=True;'
        )
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE [{entry_database.get()}]")  # Correção: Coloquei os colchetes para evitar erros no nome do banco
        connection.commit()
        cursor.close()
        connection.close()
        info_label.configure(text="Banco de Dados criado com sucesso!")
    except pyodbc.Error as ex:
        info_label.configure(text="Erro ao criar o banco de dados")

# Função para conectar ao banco de dados
def connect_db():
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            'Server=LAPTOP-VNB6KU8U\\SQLEXPRESS;'
            f'DATABASE={entry_database.get()};'  # Correção: Uso de 'DATABASE' com o nome do banco de dados
            'Trusted_Connection=True;'
        )
        connection.autocommit = True
        connection.close()
        info_label.configure(text="Conexão feita com sucesso!")
    except pyodbc.Error as ex:
        info_label.configure(text="A conexão falhou")

# Botão para criar o banco de dados
create_button = customtkinter.CTkButton(app, text="Criar",
                                        command=create_db,
                                        fg_color="pink")
create_button.place(relx=0.3, rely=0.4)

# Botão para conectar ao banco de dados
connect_button = customtkinter.CTkButton(app, text="Conectar",
                                         command=connect_db,
                                         fg_color="purple")
connect_button.place(relx=0.3, rely=0.5)

# Label para exibir mensagens de status
info_label = customtkinter.CTkLabel(app, text="")
info_label.place(relx=0.1, rely=0.6)

# Iniciar a interface gráfica
app.mainloop()
