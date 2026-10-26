def iniciar_jogo():
    print("==============================")
    print("      JOGO DE SEQUÊNCIA")
    print("==============================")
    print("Organize os números em ordem!")
    print("Use W, A, S e D para movimentar.")
    print("Digite Q para sair.")
    print("==============================")


def mostrar_tabuleiro(tabuleiro):
    for i in range(0, len(tabuleiro), 3):
        linha = tabuleiro[i:i + 3]
        print(" | ".join(str(numero) if numero != 0 else "_" for numero in linha))
        print("-" * 13)


def mover_peca(tabuleiro, movimento):
    posicao_vazia = tabuleiro.index(0)
    nova_posicao = posicao_vazia

    if movimento == "w" and posicao_vazia >= 3:
        nova_posicao -= 3

    elif movimento == "s" and posicao_vazia < 9:
        nova_posicao += 3

    elif movimento == "a" and posicao_vazia % 3 != 0:
        nova_posicao -= 1

    elif movimento == "d" and posicao_vazia % 3 != 2:
        nova_posicao += 1

    else:
        print("Movimento inválido!")
        return

    tabuleiro[posicao_vazia], tabuleiro[nova_posicao] = (
        tabuleiro[nova_posicao],
        tabuleiro[posicao_vazia],
    )


def jogar():
    tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 0, 10, 11, 9]

    iniciar_jogo()

    while True:
        mostrar_tabuleiro(tabuleiro)

        movimento = input("Seu movimento: ").lower().strip()

        if movimento == "q":
            print("Jogo encerrado.")
            break

        mover_peca(tabuleiro, movimento)


if __name__ == "__main__":
    jogar()