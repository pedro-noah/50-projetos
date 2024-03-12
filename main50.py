import random
import os
import time

#FUNÇÕES MENU
def titulo_projeto():
    print('''\033[1;36m
        
█▀ █▀█   █▀█ █▀█ █▀█ ░░█ █▀▀ ▀█▀ █▀█ █▀
▄█ █▄█   █▀▀ █▀▄ █▄█ █▄█ ██▄ ░█░ █▄█ ▄█
    \033[0m''')

def menu_principal():
    print('''
        1. Biscoito da Sorte
        2. Rolagem de Dados
        3. Pedra, Papel, Tesoura
        4. Pedra, Papel, Tesoura, Lagarto e Spock?!
        5. Quem quer ser um MILIONARIO?
        6. Quiz
        7. Aventura
    ''')

    opcao_menu_principal = int(input('Digite qual projeto deseja extrair: '))
    print()
    if opcao_menu_principal == 1:
        pjt_biscoito_sorte()
    elif opcao_menu_principal == 2:
        pjt_rolagem_dado()
    elif opcao_menu_principal == 3:
        pjt_pedra_papel_tesoura()
    elif opcao_menu_principal == 4:
        pjt_pptls()
    elif opcao_menu_principal == 5:
        pjt_milionário()
    elif opcao_menu_principal == 6:
        pjt_quiz()
    elif opcao_menu_principal == 7:
        pjt_aventura()



#FUNÇÕES DO PROJETO
def pjt_biscoito_sorte():
    dic_biscoito = [{'num': 1, 'frase':'O sucesso virá para aqueles que trabalham duro e persistem.', 'numero':'18 45 65'}, 
                {'num': 2, 'frase':'A vida é uma jornada - aproveite o caminho tanto quanto o destino.', 'numero':'88 25 60'},
                {'num': 3, 'frase':'Seja gentil sempre, pois você nunca sabe o impacto que suas palavras podem ter.', 'numero':'32 65 23'},
                {'num': 4, 'frase':'Grandes coisas muitas vezes têm começos humildes.', 'numero':'84 45 09'},
                {'num': 5, 'frase':'Acredite em si mesmo e outros também acreditarão em você.', 'numero':'75 76 45'}]
    num_biscoito = random.randrange(1, 5)
    for biscoito in dic_biscoito:
        if num_biscoito == biscoito['num']:
            print(biscoito['frase'])
            print(biscoito['numero'])
    clear()

def pjt_rolagem_dado():
    print('Jogando os dados...')
    dado1 = random.randrange(1, 6)
    dado2 = random.randrange(1, 6)
    print(f'Cairam os numeros {dado1} e {dado2}')
    print(f'O valor final foi de:  {dado2+dado1}')
    clear()

def pjt_pedra_papel_tesoura():
    opcao_ppt = input('Digite a opcao capitalizada (ALL CAPS): ')
    opcoesppt = ["PEDRA", "PAPEL", "TESOURA"]
    opcao_computador_ppt = random.choice(opcoesppt)
    
    print("O computador jogou:", opcao_computador_ppt)
    
    if opcao_ppt == opcao_computador_ppt:
        print('EMPATE!')
    elif (opcao_ppt == "PEDRA" and opcao_computador_ppt == "TESOURA") or \
         (opcao_ppt == "PAPEL" and opcao_computador_ppt == "PEDRA") or \
         (opcao_ppt == "TESOURA" and opcao_computador_ppt == "PAPEL"):
        print('GANHOU!')
    else:
        print('PERDEU!')
    clear()

def pjt_pptls():
    opcao_pptls = input('Digite a opcao capitalizada (ALL CAPS): ')
    opcoes_pptls = ["PEDRA", "PAPEL", "TESOURA", "LAGARTO", "SPOCK"]
    opcao_computador_pptls = random.choice(opcoes_pptls)
    
    print("O computador jogou:", opcao_computador_pptls)
    
    if opcao_pptls == opcao_computador_pptls:
        print('EMPATE!')
    elif (opcao_pptls == "PEDRA" and (opcao_computador_pptls == "TESOURA" or opcao_computador_pptls == "LAGARTO")) or \
         (opcao_pptls == "PAPEL" and (opcao_computador_pptls == "PEDRA" or opcao_computador_pptls == "SPOCK")) or \
         (opcao_pptls == "TESOURA" and (opcao_computador_pptls == "PAPEL" or opcao_computador_pptls == "LAGARTO")) or \
         (opcao_pptls == "LAGARTO" and (opcao_computador_pptls == "PAPEL" or opcao_computador_pptls == "SPOCK")) or \
         (opcao_pptls == "SPOCK" and (opcao_computador_pptls == "PEDRA" or opcao_computador_pptls == "TESOURA")):
        print('GANHOU!')
    else:
        print('PERDEU!')
    clear()
    
def pjt_milionário():
    perguntas_respostas = [
        {'pergunta': "Qual é a capital do Brasil?", 'resposta': "Brasília"},
        {'pergunta': "Quem escreveu 'Dom Quixote'?", 'resposta': "Miguel de Cervantes"},
        {'pergunta': "Qual é o maior planeta do sistema solar?", 'resposta': "Júpiter"},
        {'pergunta': "Quem pintou a 'Mona Lisa'?", 'resposta': "Leonardo da Vinci"},
        {'pergunta': "Quantos continentes existem?", 'resposta': "Sete"},
        {'pergunta': "Qual é a montanha mais alta do mundo?", 'resposta': "Monte Everest"},
        {'pergunta': "Quem foi o primeiro homem a pisar na Lua?", 'resposta': "Neil Armstrong"},
        {'pergunta': "Qual é o símbolo químico para o ouro?", 'resposta': "Au"},
        {'pergunta': "Quem escreveu 'Romeu e Julieta'?", 'resposta': "William Shakespeare"},
        {'pergunta': "Qual é o maior oceano do mundo?", 'resposta': "Oceano Pacífico"},
        {'pergunta': "Quem foi o primeiro presidente dos Estados Unidos?", 'resposta': "George Washington"},
        {'pergunta': "Quem foi o cientista que formulou a teoria da relatividade?", 'resposta': "Albert Einstein"},
        {'pergunta': "Qual é o segundo elemento mais abundante na crosta terrestre?", 'resposta': "Silício"},
        {'pergunta': "Quem escreveu a obra 'O Pequeno Príncipe'?", 'resposta': "Antoine de Saint-Exupéry"},
        {'pergunta': "Qual é o maior mamífero terrestre?", 'resposta': "Elefante africano"},
        {'pergunta': "Quem é o autor da obra 'A Metamorfose'?", 'resposta': "Franz Kafka"},
        {'pergunta': "Qual é a cidade mais populosa do mundo?", 'resposta': "Tóquio"},
        {'pergunta': "Quem pintou 'A Persistência da Memória'?", 'resposta': "Salvador Dalí"},
        {'pergunta': "Qual é o país com a maior área territorial do mundo?", 'resposta': "Rússia"},
        {'pergunta': "Quem foi o primeiro homem a escalar o Monte Everest?", 'resposta': "Sir Edmund Hillary"}
]

    random.shuffle(perguntas_respostas)

    soma_valor = 0
    total_soma = 0
    rodada = 1

    print("\033[1m\033[92m=== Bem-vindo ao Python Millionaire ===\033[0m")


    for pergunta in perguntas_respostas:
        print(f'Comecamos a rodada {rodada}...\n')
        print((pergunta['pergunta']))
        resposta = input("RESPOSTA: ")
        
        if resposta == pergunta['resposta']:
            print("\nAcertou!")
            if rodada == 1:
                soma_valor = 100
            soma_valor *= 2
            total_soma += soma_valor
            opcao_milionario = int(input(''' 
            Digite [1] para CONTINUAR
            Digite [2] para DESISTIR      
                                    
            '''))
            
            if opcao_milionario == 1:
                rodada+=1
                continue
            else:
                print("\nVoce parou!")
                break
        else:
            print("\nErrou!!!")
            soma_valor = 0
            break
        
        
    print(f'O valor final foi de R${soma_valor},00!')

def pjt_quiz():
    perguntas_resp = [
    {'pergunta': 'Qual a terceira pessoa do plural?', 'opcao_errada1': 'Ele', 'opcao_errada2': 'Nós', 'opcao_errada3': 'Vós', 'opcao_correta': 'Eles'},
    {'pergunta': 'Qual é o planeta mais próximo do Sol?', 'opcao_errada1': 'Vênus', 'opcao_errada2': 'Marte', 'opcao_errada3': 'Júpiter', 'opcao_correta': 'Mercúrio'},
    {'pergunta': 'Qual é a capital da França?', 'opcao_errada1': 'Madrid', 'opcao_errada2': 'Berlim', 'opcao_errada3': 'Londres', 'opcao_correta': 'Paris'}]
    
    rodada = 1
    pontuacao = 0
    letras = ['A', 'B', 'C', 'D']

    for pergunta in perguntas_resp:
        print(f'\nRodada: {rodada} de 3\n')
        print(f'{rodada}. {pergunta["pergunta"]}')
        rodada += 1
        print('\nOPCOES\n')
        opcoes = [(pergunta['opcao_errada1']), (pergunta['opcao_errada2']), (pergunta['opcao_errada3']), (pergunta['opcao_correta'])]
        random.shuffle(opcoes)
        for letra, opcao in zip(letras, opcoes):
            print(f'[{letra}] - {opcao}')
        
        resposta_correta = letras[opcoes.index(pergunta['opcao_correta'])]
        resposta = input("Digite a letra da resposta: ").upper()
        if resposta == resposta_correta:
            print('\nAcertou!')
            pontuacao += 1
        else:
            print('\nErrou!')
            print(f'A resposta era {pergunta["opcao_correta"]}')

    print(f'\nPontuacao final de {pontuacao}')
            
def pjt_aventura():
    print('SEJA BEM VINDO A CAVERNA DO DRAGÃO!\n')
    print('''
    Como jogar?
    Primeiro você lê a situação em que está envolvido, 
    depois seleciona uma de duas opções para seguir.
                
    Lembre-se que qualquer decisão errada pode fazer você perder o jogo!
            
    Boa sorte, aventureiro!\n
    ''')
    print('*' * 60)
    print('''\n
    Você se encontra na frente da entrada da caverna do dragão...
    [1] Você entra na caverna
    [2] Você decide dar meia volta e sair dali
    ''')

    opcao_caverna = int(input("\nOPÇÃO: "))
    print('Voce segue para dentro da caverna...') if opcao_caverna == 1 else exit('Game Over')

    print('''\n
    Você encontra duas portas com símbolos, a da esquerda tem um dragão, a da direita tem um tesouro
    [1] Você entra na porta do dragão
    [2] Você entra na porta do tesouro
    ''')

    opcao_porta = int(input("\nOPÇÃO: "))
    if opcao_porta == 1:

    
    
    
#INICIALIZADORES
def clear():
    x = input('''
        Digite ENTER para continuar...
        Digite 1 depois ENTER para fechar
        ''')
    if x == "1":
        exit()
    else:
        os.system('cls')
        main()

def main():
    titulo_projeto()
    menu_principal()

if __name__ == "__main__":
    main()

