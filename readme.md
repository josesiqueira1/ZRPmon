# ZRPmon

Uma aplicação que consulta e retorna as habilidades em ordem afabética de um pokemon

## Dependências

* [requests](https://pypi.org/project/requests/)

A instalação das dependências pode ser realizada exectutando o comando abaixo:

`pip install -r requirements.txt`

## Execução

Para executar a aplicação é necessário rodar o comando:

`python main.py`

## Utilização

### URL

Utilizar a seguinte sintaxe:

`http://localhost/pokemon/{nome_do_pokemon}`

Exemplo:

`http://localhost/pokemon/charmander`

Exemplo de retorno

`['blaze', 'solar-power']`

## Sugestão para otimização

### Persistir dados

* Pode ser realizado a persistência dos dados em um banco de dados sqlite para realizar a consulta antes de fazer a
requisição para a API
* Utilizar uma biblicoteca para a consulta e também para o cache dos dados