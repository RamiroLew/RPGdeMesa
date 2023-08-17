#Principais funcionalidades do codigos estarão nesta pagina:
#from tabulate import tabulate
from random import randint

def dado(valor):     # Fará a ação de sortear um numero desejavel.
    #lados = int(input('Quantos lados terá o dado? '))
    resultado = int(randint(1, valor))
    return resultado
def titulo(txt):
    print('-' * 42)
    print(txt.center(42))
    print('-' * 42)
def cabeçalho(txt):
    print('-*' * 21)
    print(txt.center(42))
    print('-*' * 21)
def leiaInt(txt):
    while True:
        try:
            a = int(input(txt))
            return a
        except:
            print('\033[0;31mValor inserido não é um numero válido, tente novamente: \033[m')
def cadastro():
    jogadores = list()
    player = dict()
    pessoas = leiaInt('Quantas Players vão batalhar? ')
    for a in range(pessoas):  # Cadastrando os Jogadores.
        player['codigo'] = a + 1
        player['nome'] = str(input(f'Digite o >> Nome << do {a + 1}° jogador: ')).capitalize()
        player['vida'] = leiaInt(f'Quantos pontos de >> vida << o {player["nome"]} tem? ')
        player['dano'] = leiaInt(f'Qual é o >> dano << da arma de {player["nome"]}? ')
        res_armadura = 'Digite 1 para armadura leve /' \
                       ' 2 para armadura media /' \
                       ' 3 para armadura pesada /' \
                       ' 0 para armadura inexistente. '
        print(res_armadura)
        while True:
            armadura = leiaInt(f'Qual a armadura de {player["nome"]}: ')
            if armadura in (0, 1, 2, 3):
                match armadura:
                    case 0:
                        player['armadura'] = 0
                        break
                    case 1:
                        player['armadura'] = 2
                        break
                    case 2:
                        player['armadura'] = 4
                        break
                    case 3:
                        player['armadura'] = 6
                        break
                    case _:
                        print('Codigo invalido, por favor tente novamente.',
                              res_armadura)
            else:
                print('armadura não cadastrada, tente novamente. ')
        jogadores.append(player.copy())
        titulo(f'Jogador {player["nome"]} cadastrado...')
    return jogadores
'''def batalha():
    print(f'vez do jogador {jogadores[c]}')
    alvo = int(input('quem deseja atacar? (digite o cod do alvo) '))
    dano = int(input('Jogue seu dado de dano e insira o valor aqui: '))'''



