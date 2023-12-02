import pyodbc

def conectar_banco():
    # Substitua o nome do seu servidor e banco de dados
    server = 'servidor'
    database = 'banco de dados'

    try:
        # Usando 'Trusted_Connection=yes' para autenticação do Windows
        conexao = pyodbc.connect(
        f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        )
        return conexao
    except pyodbc.Error as ex:
        print(f"Erro na conexão com o banco de dados: {ex}")
        return None


def fechar_conexao(conexao):
    try:
        conexao.close()
    except pyodbc.Error as ex:
        print(f"Erro ao fechar a conexão com o banco de dados: {ex}")