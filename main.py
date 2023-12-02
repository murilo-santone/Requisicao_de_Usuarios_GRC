from database import conectar_banco, fechar_conexao
from api_requests import obter_chave_api, realizar_refresh_usuario
import pyodbc


def consultar_usuarios_com_notas_pendentes():
    conexao = conectar_banco()
    if conexao:
        try:
            cursor = conexao.cursor()
            # adicione sua consulta sql para coletar e fazer um refresh via API do usuário.
            cursor.execute("""sua consulta retornando apenas o usuário aqui""")
            usuarios_com_notas_pendentes = [str(row[0]).lstrip('0') for row in cursor.fetchall()]
            return usuarios_com_notas_pendentes
        except pyodbc.Error as ex:
            print(f"Erro na consulta ao banco de dados: {ex}")
        finally:
            fechar_conexao(conexao)


def main():
    try:
        # Consulta usuários com notas pendentes
        usuarios_pendentes = consultar_usuarios_com_notas_pendentes()

        # Para cada usuário com notas pendentes, obtem a chave e realiza o refresh
        for usuario_id in usuarios_pendentes:
            chave_api = obter_chave_api(usuario_id)
            if chave_api:
                # Realiza o refresh do usuário para notas GRC usando a chave obtida
                realizar_refresh_usuario(chave_api, usuario_id)
    except Exception as ex:
        print(f"Ocorreu um erro inesperado: {ex}")
    finally:
        print("Fechando a conexão com o banco de dados.")

if __name__ == "__main__":
    main()
