# Sistema de gerenciamento de lugares teatro

import teather_config
import teather_initializer
import reserve_seat

print(
"""
[1] - Iniciar o Teatro: Usuário informa quantas linhas e colunas ocupar, respeitando limites e sem espetáculo aberto.

[2] - Reservar Lugar: Usuário reserva lugar; paga 30% se disponível, troca se reservado.

[3] - Comprar Lugar: Pagar valor cheio se livre, 70% se reservado.

[4] - Liberar Lugar: Troca status para livre, subtrai pagamento.

[5] - Listar Poltronas: Mostra livres, reservadas e vendidas.

[6] - Encerrar Espetáculo: Se 60% ocupado, exibe vendas, reservas, livres.

[7] - Reiniciar Espetáculo: Todas as variáveis são redefinidas e as cadeiras do espetáculo são liberadas.
"""
)

print("- "*50)

while True:
        
    option = int(input("Selecione uma das opções: "))

    if option == 1 and teather_initializer.theather_status == False:

        if teather_initializer.initializer(
            int(input("Digite o número de linhas: ")),
            int(input("Digite o número de colunas: "))
            ):

            print("Teatro iniciado")
        else:
            print("***Teatro não iniciado***")
            print("- "*50)

    elif option == 1 and teather_initializer.theather_status == True:
        print("Teatro já inicializado")

    elif option == 2:
        print("Reservar lugar:")
        reserveSeatRow = int(input("Informe a linha: "))
        reserveSeatColumn = int(input("Informe a coluna: "))
        reserve_seat.reserve(reserveSeatRow, reserveSeatColumn)