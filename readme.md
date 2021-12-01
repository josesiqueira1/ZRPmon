# ZRPmon

Uma aplicação que consulta e retonrna as habilidades dos pokemons em ordem afabética

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