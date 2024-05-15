#To-Do List Django
Este é um aplicativo simples de lista de tarefas desenvolvido em Django. Ele permite que os usuários criem, visualizem, atualizem e excluam tarefas.

Funcionalidades
Adicionar novas tarefas.
Marcar tarefas como concluídas.
Editar o conteúdo das tarefas.
Excluir tarefas.
Configuração do Ambiente de Desenvolvimento
Para configurar e executar o projeto em seu ambiente de desenvolvimento local, siga estas etapas:

Certifique-se de ter o Python (preferencialmente Python 3.x) instalado em seu sistema.
Clone este repositório em sua máquina local.

Navegue até o diretório raiz do projeto:

cd to_do_list_django

Crie um novo ambiente virtual para o projeto:

python -m venv env

Ative o ambiente virtual. No Windows, execute:

env\Scripts\activate

No Linux/macOS, execute:

source env/bin/activate

Instale as dependências do projeto:

pip install -r requirements.txt

Execute as migrações do banco de dados:

python manage.py migrate

Inicie o servidor de desenvolvimento:

python manage.py runserver

O aplicativo estará disponível em http://127.0.0.1:8000/.

Contribuindo
Se você quiser contribuir com este projeto, sinta-se à vontade para enviar pull requests ou relatar problemas nas issues.
