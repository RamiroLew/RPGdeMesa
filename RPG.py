from lib.funções import *
from tabulate import tabulate
cabeçalho('Iniciando Batalha para RPG de mesa')
jogadores = cadastro()
tabela = tabulate(jogadores, headers="keys", tablefmt="grid")
print(tabela)
cabeçalho('>>Iniciando Batalha simples automatica!!<<')
while True:         # loop de batalha
    contador = 0
    for c in range(len(jogadores)):
        print(f'vez do jogador {jogadores[c]["nome"]}')
        while True:         # condição de existencia do alvo
            alvo = leiaInt('quem deseja atacar? (digite o cod do alvo) ') - 1
            if alvo < len(jogadores) + 1:
                print('Jogador(a) não encontrado, por favor, tente novamente')
            else:
                break
        dano = dado(jogadores[c]['dano'])
        print(f'Após rodar um >D{jogadores[c]["dano"]}< da arma, saiu {dano} no dado')
        armadura = dado(jogadores[alvo]['armadura'])
        print(f'A armadura aparou {armadura} de dano do ataque')
        dano -= armadura
        if dano < 0:
            dano = 0
        jogadores['vida'] -= dano
        print(f'O jogador(a) {jogadores[alvo]}, ficou com {jogadores[alvo]["vida"]}')
    contador += 1
    r = str(input(f'A {contador}° rodada acabou, desejam continuar? ')).lower()
    if r == 'nao':
        break

