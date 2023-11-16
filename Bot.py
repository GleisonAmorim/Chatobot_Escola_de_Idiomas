import os

def processar_resposta(resposta, nome, email):
    if resposta == '1':
        print(f'{os.linesep}Olá, {nome}! Nossos cursos de oferecem uma abordagem abrangente para iniciantes. Para mais informações, confira nosso site: www.escoladeidiomas.com.br ou entre em contato pelo e-mail: esoladeidiomas@gmail.com {os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}Caro {nome}, nossos instrutores são altamente qualificados para garantir que você atinja seus objetivos no aprendizado de idiomas.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, oferecemos aulas presenciais e online para a sua conveniência. Você pode escolher a opção que melhor se adapta ao seu estilo de aprendizado.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, o preço dos cursos varia de acordo com a duração e o tipo de aula. Recomendo verificar nossa página de preços em nosso site ou agendar uma consulta para obter informações mais detalhadas.{os.linesep}')
    elif resposta.lower() == 'sair':
        print(f'{os.linesep}Obrigado por conversar conosco, {nome}! Até logo.{os.linesep}')
        exit()
    else:
        print(f"{os.linesep}Selecione uma opção válida! Ou digite 'sair' para encerrar a conversa.{os.linesep}")

def start():
    # Apresentar o chatbot
    print(f"Olá, seja bem-vindo ao Chatbot da Escola de Idiomas!{os.linesep}")
    # Pedir o nome
    nome = input("Digite seu nome: ")
    # Pedir o e-mail
    email = input("Digite seu E-mail: ")

    while True:
        # Oferecer o menu de opções
        resposta = input(f'{os.linesep}O que você gostaria de saber hoje?\n{os.linesep}[1] - Como são os cursos para iniciantes?\n{os.linesep}[2] - Qualificação dos instrutores\n{os.linesep}[3] - Modalidades de aulas (presencial/online)\n{os.linesep}[4] - Informações sobre preços\n{os.linesep}[sair] - Encerrar a conversa\n{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome, email)

if __name__ == "__main__":
    start()
