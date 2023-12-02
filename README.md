# Requisicao_de_Usuarios_GRC
Esse projeto foi criado com intuito de automatizar o processo de realizar a requisição de usuário por usuário manualmente, afim de ser realizado automaticamente ao executar apenas um arquivo.

Dentre os arquivos irei falar sobre cada um:

database.py > Realiza a configuração de conexão com o banco de dados.

api_request > Neste arquivo você adiciona as configurações que seram utilizadas para realizar a requisição, dentro dele tem duas funções, uma que é possível coletar um token apartir da API informada e a outra função é possível realizar o insert desse token para que seja realizado um reprocessamento do usuário neste caso do arquivo.

main.py > Arquivo principal que chamara todas as funções dos arquivos terceiros para que seja feito um processo de cada vez por usuário, você também poderá colocar sua query para coletar o usuário e também verá uma condição que realiza um for iterando sobre o retorno dos usuários.
