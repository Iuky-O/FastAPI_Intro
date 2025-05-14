import io                                       #para abrir os arquivos já com verificação de caractere
import os                                       #para lidar com operações com arquivos
from setuptools import find_packages, setup     # find_packages para encontrar os pacotes e setup para configurar a instalação do projeto


def read(*paths, **kwargs): #significa passar vários "pedaços" de caminho de pasta/arquivo
    """Função para ler arquivos(README, requirements.txt, etc)"""
    content = ""                                         #atribuindo ela vazia para preencher com o conteúdo lido
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths), #pegando o diretório que tá o setup.py
        encoding=kwargs.get("encoding", "utf8")          #definindo como os bytes são convertidos em texto legível (encoding, por padrão ‘web’: utf8)
    ) as open_file:                                      #chamando esse arquivo que li com with io de "open_file"
        content = open_file.read().strip()               #guardando o conteúdo lido com .read() e tirando espaços em branco com strip()
    return content


def read_requirements(path):
    return[
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="fastapiZero",
    version="0.1.0",
    description="Tentando fazer uma fastapi",
    url="localhost/8080",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["app = app.cli:main"]
    }
)


#"include_packages_data=True" para incluir arquivos que não são ".py" também
#"entry_points" para criar comandos no terminal ex: ""app --help" (dizendo para importar o main do cli caso usemos)