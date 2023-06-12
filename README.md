# Party Pass Web

Este é um projeto web desenvolvido em Python com o framework Django para fazer o gerenciamento de clientes, produtos e comandas.
Foi desenvolvido durante a atividade final da disciplina de Desenvolvimento para Web, sob a orientação do Professor Wildson Caio Felipe.
A equipe é composta pelos estudantes da 4ª Fase do Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas na instituição Faculdade de Tecnologia Senac Palhoça:
[Ana Flávia de Freitas Corrêa](https://github.com/AnaFlaviaCorrea)
[Natália Heinzen](https://github.com/natalia-hnzn)
[Pedro Paulo de Abreu](https://github.com/pdropaullo)
[Thiago Ruan Costa](https://github.com/Thiagor34)

## Funcionalidades

- Cadastrar, Pesquisar, Editar e Excluir Produtos
- Cadastrar e Pesquisar Clientes
- Recarregar Comanda
- Realizar Consumo

## Requisitos

- Python
- Django

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/pdropaullo/Party_Pass_Web.git

2. Acesse o diretório do projeto:

cd Party_Pass_Web

3. Crie e ative um ambiente virtual (recomendado):

python -m venv venv
.\venv\Scripts\activate

4. Instale as dependências:

pip freeze > requirements.txt

5. Execute as migrações do banco de dados:

python manage.py migrate

6. Inicie o servidor:

python manage.py runserver

7. Acesse o aplicativo no seu navegador em http://http://127.0.0.1:8000/.