import httplib, json

# Aqui ele abre o arquivo "testehttp.txt".
conteudo = open('./testehttp.txt', "rb")

# Cria o vetor "dados".
dados = {}

# Coloca o conteudo do arquivo em uma variavel dentro do vetor "dados".
dados["relatorio"] = conteudo.read()

# Fecha o arquivo "testehttp.txt".
conteudo.close()

# Codifica o vetor em texto usando json.
dados = json.dumps(dados)

# Define os headers do protocolo HTTP para stream (transferencia de arquivos / texto).
headers = {
        "Content-type": "application/octet-stream",
        "Accept": "text/plain"
}

# Abre a conexao com o meu servidor "2br.com.br".
conexao = httplib.HTTPConnection("2br.com.br")

# Define o tipo de conexao (POST), caminho do arquivo no servidor, a variavel de dados, e define os headers.
conexao.request("POST", "/outros/wilson.php", dados, headers)

# Aqui ele traz o retorno da conexao HTTP para a variavel "retorno".
retorno = conexao.getresponse()

# Visualizacao da variavel retorno, com o conteudo enviado pelo servidor.
print retorno.read()

# Fecha a conexao com o servidor.
conexao.close()