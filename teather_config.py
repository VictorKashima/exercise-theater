# Configuração da arquibancada

roomRow = int(input("Digite o número de linhas (Máximo: 300): "));
if roomRow < 0 or roomRow > 300:
    while True:
        roomRow = 0
        roomRow = int(input("Digite o número de linhas (Máximo: 300): "));
        if roomRow >= 0 and roomRow <= 300:
            break

roomColumn = int(input("Digite o número de colunas (Máximo: 300): "));
if roomColumn < 0 or roomColumn > 300:
    while True:
        roomColumn = 0
        roomColumn = int(input("Digite o número de colunas (Máximo: 300): "));
        if roomColumn >= 0 and roomColumn <= 300:
            break

ticketPrice = float(input("Digite o valor do ingresso inteiro: "));

room = []

for i in range(roomRow):
    room.append([])
    for j in range(roomColumn):
        room[i].append(0)

def showRoom():
    for k in range(roomRow):
        print(room[k])