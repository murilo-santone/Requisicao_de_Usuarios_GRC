import requests


# Função que irá obter a chave para realizar refresh
def obter_chave_api(usuario_id):
    try:
        # Substitua a URL e outros parâmetros conforme necessário
        url = 'https://www.www.www/chave'
        # altere para o padrão do body usado na API
        payload = {
            'campo1': 'x',
            'ambiente': 99,
            'usuario': usuario_id,
            'senha': 'xxx'
        }

        # Faz a solicitação para obter a chave
        response = requests.post(url, json=payload)
        response.raise_for_status()

        chave_api = response.json().get('chave') # 'chave' é o nome do campo que está retornando a chave na API (format json)
        return chave_api
    except requests.exceptions.RequestException as ex:
        print(f"Erro ao obter chave para o usuário {usuario_id}: {ex}")
        return None


def realizar_refresh_usuario(chave_api, usuario_id):
    try:
        # Substitua a URL e outros parâmetros conforme necessário
        url = 'https://www.www.www/chave'
        # Aqui será adicionado a chave coletada
        headers = {
            'Authorization': f'Bearer {chave_api}',  # chave
            'Content-Type': 'application/json'  # descreve o formato que recebera a chave
        }

        # altere para o padrão do body usado na API
        payload = {
            'campo1': 'x',
            'ambiente': 99,
            'usuario': usuario_id,
            'senha': 'xxx'
        }

        # Faz a solicitação para realizar o refresh do usuário
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        print(f"Refresh do usuário {usuario_id} concluído com sucesso.")
    except requests.exceptions.RequestException as ex:
        print(f"Erro ao realizar refresh do usuário {usuario_id}: {ex}")