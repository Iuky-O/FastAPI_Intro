# Tô testando para fazer a aplicação. Só que precisamos de uma venv por igual para trabalhar.
## Então agt vai precisar de uns requisitos para desenvolvedores, na venv, assim o nosso ambiente virtual vai ficar por igual.

## Notem o requirements-dev.txt ele vai ter ferramentas de desenvolvedor de base para nos

## A mais importante é a pip-tools

## Para rodar precisa ativar a venv e depois usar

```shell
    pip-compile requirements.in
```

````shell
    pip install -r requirements-dev.txt
````



## Precisamos do pip-tools para usar o pip-compile, ele vai compilar o arquivo requirements.in
# O requirements.in é bem basico, o pip-compile vai usar ele para criar o requirements.txt

## A partir daqui a agt pode só mudar o requirements.in adicionando novas bibliotecas importantes pro o nosso sistema.
## É muito importante que quando formos compilar de novo para requirements.txt. Usemos pip-compile sem o "--upgrade". Porque se não vai atualizar as bibliotecas e o nosso sistema pode cair

# Agora vamos instalar a aplicação

# Ative a venv e rode

````shell
pip install -e .
````

## Ele diz para o pip procurar os metadados que estão na raiz do meu projeto
## O que ele acaba encontrando em setup.py, que tem todo aquele caminho para ler e instalar os requirements da nossa aplicação

# Pode rodar pip list para ver tudo instalado, inclusive a aplicação

````shell
pip list
````

## O que deve retornar uma lista gigantesca

# Definindo sessões com varáveis de ambiente para o nosso projeto
## Usaremos o Dynaconf que já foi instalado na aplicação para criar as nossas variáveis de ambiente para manipular o nosso sistema

## No arquivo "default.toml" estão as variáveis de ambiente do sistema de acordo com sessões
### Ex: Futuramente poderemos apenas mudar o ambiente como "default", "production" e atualizar o sistema