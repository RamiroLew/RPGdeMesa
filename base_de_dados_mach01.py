from random import randint
print('automatizando CAMPO DE BATALHA')
pessoas = int(input('Quantas pessoas estarão batalhando? '))
print('>>> Cadastrando Lutadores <<<')
print('ps: ordem de batalha será do primeiro cadastrado para o ultimo')
player = {}
jogadores = []
for a in range(pessoas):  # DADOS DO PLAYER
    player['nome'] = str(input(f'Digite o Nome do {a + 1}° jogador: ')).capitalize()
    player['vida'] = int(input(f'Quantos pontos de vida o {player["nome"]} tem? '))
    print('Digite 1 para armadura leve / 2 para armadura media / 3 para armadura pesada / 0 para armadura inexistente. ')
    player['armadura'] = int(input(f'Qual a armadura de {player["nome"]}: '))
    if player['armadura'] == 1:
        player['armadura'] = 2
    elif player['armadura'] == 2:
        player['armadura'] = 4
    elif player['armadura'] == 3:
        player['armadura'] = 6
    player['arma'] = int(input(f'Qual o dano da arma de {player["nome"]}? '))
    jogadores.append(player.copy())
    print(f'jogador {player["nome"]} cadastrado...')
print('-='*35)
print(jogadores)
print('-='*35)
print('cod: ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print('-*'*35)
for k, v in enumerate(jogadores):
    print(f'{k:>3}:', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-*'*35)
print('>>> BATALHA <<< ')
print()
cont = 0
a = 0
while True:
    for c in range(len(jogadores)):
        if jogadores[c]['vida'] <= 0:
            print(f'jogador {jogadores[c]} morto!')
            jogadores[c].clear()
            break
        print(f'vez do jogador {jogadores[c]}')
        alvo = int(input('quem deseja atacar? (digite o cod do alvo) '))
        dano = int(input('Jogue seu dado de dano e insira o valor aqui: '))
        if dano == 999:
            dano = randint(1, jogadores[c]['arma'])
            print(f'O valor sorteado foi de {dano}')
        armadura = int(input('Jogue o dado da armadura e insira aqui: '))
        if armadura == 999:
            armadura = randint(1, jogadores[alvo]['armadura'])
            print(f'O valor defendido pela armadura foi {armadura}')
        dano -= armadura
        if dano > 0:
            jogadores[alvo]['vida'] -= dano
        print(f'o Jogador {jogadores[alvo]["nome"]} tomou {dano} de dano. vida restante {jogadores[alvo]["vida"]}')
        print('-='*35)
    cont += 1
    print(f'>>> Final do {cont}° Round <<<')
    for k, v in enumerate(jogadores):
        print(f'{k:>3}:', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()
    r = str(input('deseja continuar? [S/N] '))
    if r in 'nN':
        break

