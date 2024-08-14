def cria_tabuleiro():
    # Inicializa o tabuleiro 3x3 com zeros
    tabuleiro = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    # [[0, 0, 0] for _ in range(3)]
    return tabuleiro


def exibe_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print()
        print(f'{linha[0]} | {linha[1]} | {linha[2]}')
        print("__________")


def verifica_ganhador(tabuleiro):
    # Verifica linhas, colunas e diagonais
    for i in range(3): # Colocar and depois
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != 0:
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != 0:
            return tabuleiro[0][i]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != 0:
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != 0:
        return tabuleiro[0][2]
    return


def main():
    tabuleiro = cria_tabuleiro()
    jogador = 1

    while True:
        exibe_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador}, escolha a linha (1 a 3): ")) - 1
        coluna = int(input(f"Jogador {jogador}, escolha a coluna (1 a 3): ")) - 1

        # * Colocar X ou O Dependendo do jogador
        if tabuleiro[linha][coluna] == 0:
            if jogador == 1:
                tabuleiro[linha][coluna] = "X"
            else:
                tabuleiro[linha][coluna] = "O"
            ganhador = verifica_ganhador(tabuleiro)

            if ganhador:
                exibe_tabuleiro(tabuleiro)
                print(f"Jogador {ganhador} venceu!")
                break

            # * Alterna entre jogador 1 e 2
            if jogador == 1:  # podemos criar uma função
                jogador = 2
            else:
                jogador = 1
        else:
            print("Posição já ocupada. Tente novamente.")
        # Colocar velha


if __name__ == "__main__":
    main()
