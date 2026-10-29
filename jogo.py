def iniciar_jogo():
    print("==============================")
    print("     JOGO DE SEQUÊNCIA")
    print("==============================")
    print("Organize os números em ordem!")
    print("Em breve, você poderá jogar.")
    print("==============================")


def criar_tabuleiro():
    # Cria uma matriz 4x4 (4 linhas e 3 colunas) com os números de 1 a 11 e um espaço vazio (" ")
    tabuleiro = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, " "]
    ]
    return tabuleiro

def exibir_tabuleiro(tabuleiro):
    print("\n  +-----+-----+-----+")
    for linha in tabuleiro:
        # Formata cada elemento para alinhar perfeitamente no terminal
        elementos_formatados = []
        for elemento in linha:
            elementos_formatados.append(f"{str(elemento):>2}")
        
        print("  | " + " | ".join(elementos_formatados) + " |")
        print("  +-----+-----+-----+")
    print()

tabuleiro = criar_tabuleiro()
exibir_tabuleiro(tabuleiro)

print("Em breve, você poderá jogar.")
print("==============================")

if __name__ == "__main__":
    iniciar_jogo()

def mover_peca(tabuleiro, movimento):
    posicao_vazia = tabuleiro.index(0)
    nova_posicao = posicao_vazia

    if movimento == "w":
        if posicao_vazia >= 3:
            nova_posicao -= 3
        else:
            print("Movimento inválido! Não há espaço acima.")
            return False

    elif movimento == "s":
        if posicao_vazia < 9:
            nova_posicao += 3
        else:
            print("Movimento inválido! Não há espaço abaixo.")
            return False

    elif movimento == "a":
        if posicao_vazia % 3 != 0:
            nova_posicao -= 1
        else:
            print("Movimento inválido! Não há espaço à esquerda.")
            return False

    elif movimento == "d":
        if posicao_vazia % 3 != 2:
            nova_posicao += 1
        else:
            print("Movimento inválido! Não há espaço à direita.")
            return False

    else:
        print("Tecla inválida! Use W, A, S ou D.")
        return False

    tabuleiro[posicao_vazia], tabuleiro[nova_posicao] = (
        tabuleiro[nova_posicao],
        tabuleiro[posicao_vazia],
    )

    return True