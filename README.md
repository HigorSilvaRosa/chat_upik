# Chat Upik

## Sobre
Essa aplicação é um teste simples de implementação de um chat em Django com suporte à API de WebSocket.
Existe a possbilidade de crição de várias salas de bate papo e todas as mensagens são recebidas em tempo real.

## Implememtação de WebSocket

Para implementar WebSocket em Django foi utilizado um pacote Python chamado **django-omnibus**. O pacote **django-omnibus** não necessita de outras dependências e por isso torna a implementação bem simples.

## Como executar
Primeiro tenha em mente que você precisa ter o virtualenv e o Python 3 instaldo em sua máquina.

Clone o proejto

    git clone https://github.com/HigorSilvaRosa/chat_upik.git

Crie um ambiente virtual Python 3

    virtualenv -p python3 chat_upik_env

Ative o ambiente virtual

    source chat_upik_env/bin/activate

Entre no diretório do projeto

    cd chat_upik

Instale as dependências do pip

    pip install -r requirements.txt
    
Execute as migrações

    python manage.py migrate

Inicie o serviço para trabalhar com WebSokets

     python manage.py omnibusd

Você também precisa iniciar o servidor de desenvolvimento Django

    python manage.py runserver
    
Tanto o serviço de WebSokets quanto o servidor de desenvolvimento precisam executar simultaneamente. Você pode fazer isso facilmente usando terminais.
