import random
import os
import time

#FUNÇÕES MENU
def titulo_projeto():
    print('''
        
█▀ █▀█   █▀█ █▀█ █▀█ ░░█ █▀▀ ▀█▀ █▀█ █▀
▄█ █▄█   █▀▀ █▀▄ █▄█ █▄█ ██▄ ░█░ █▄█ ▄█
    ''')

def menu_principal():
    print('''
        1. Biscoito da Sorte
        2. Rolagem de Dados
        3. Pedra, Papel, Tesoura
        4. Pedra, Papel, Tesoura, Lagarto e Spock?!
        5. Quem quer ser um MILIONARIO?
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
    {'pergunta': "Quantos continentes existem?", 'resposta': "Sete"}
    ]
    random.shuffle(perguntas_respostas)
    soma_valor = 100
    for pergunta in perguntas_respostas:
        print((pergunta['pergunta']))
        resposta = input("RESPOSTA: ")
        if resposta == pergunta['resposta']:
            print("Acertou!")
            soma_valor *= 2
            opcao_milionario = int(input(''' 
            Digite [1] para CONTINUAR
            Digite [2] para DESISTIR      
                                   
            '''))
            if opcao_milionario == 1:
                continue
            else:
                print("Voce parou!")
                
                break
            continue
        else:
            print("Errou!")
            soma_valor = 0
            break
    print(f'O valor final foi de R${soma_valor},00!')

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

