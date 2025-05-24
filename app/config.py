import os

from dynaconf import Dynaconf                               #Dynaconf para carregar os arquivos .toml e .env e permitir acessar configs(também suporta múltiplos ambientes)

HERE = os.path.dirname(os.path.abspath(__file__))           #carregando o caminho absoluto para garantir que os arquivos de config sejam encontrados(Virou apenas a variável HERE, homenagem ao Linux)

settings = Dynaconf(                                        #criando o objeto settings de Dynaconf
    envvar_prefix="app",                                    #definindo o nosso prefixo para variáveis de ambiente(APP__)
    preload=[os.path.join(HERE, "default.toml")],           #informando o arquivo de config base que deve ser carregado antes de todos(preload)
    settings_files=["settings.toml", ".env"],                        #dizendo quais os arquivo de configurações sensíveis
    environments=["development", "production", "testing"],  #definindo ambientes disponíveis na aplicação (depois podemos ativar como APP_ENV=production)
    env_switcher="APP_ENV",                                 #nome da variável de ambiente que ativa nosso ambiente virtual(exemplo de cima)
    load_dotenv=True,                                      #Dizendo para não carregar automaticamente arquivos .env
)