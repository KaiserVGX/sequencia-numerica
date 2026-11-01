def iniciar_jogo():
    print("==============================")
    print("      JOGO DE SEQUÊNCIA")
    print("==============================")
    print("Organize os números em ordem!")
    print("Use W, A, S e D para movimentar.")
    print("Digite H para ver a ajuda.")
    print("Digite Q para sair.")
    print("==============================")


def mostrar_tabuleiro(tabuleiro):
    print()
    for i in range(0, len(tabuleiro), 3):
        linha = tabuleiro[i:i + 3]

        print(" | ".join(
            str(numero) if numero != 0 else "_"
            for numero in linha
        ))
        print("-" * 13)
    print()


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
        print("Movimento inválido!")
        return False

    tabuleiro[posicao_vazia], tabuleiro[nova_posicao] = (
        tabuleiro[nova_posicao],
        tabuleiro[posicao_vazia],
    )

    return True


def verificar_vitoria(tabuleiro):
    sequencia_correta = list(range(1, 12)) + [0]
    return tabuleiro == sequencia_correta


def mostrar_ajuda():
    print("\n========== AJUDA ==========")
    print("W - Mover para cima")
    print("S - Mover para baixo")
    print("A - Mover para a esquerda")
    print("D - Mover para a direita")
    print("H - Mostrar ajuda")
    print("Q - Sair do jogo")
    print("===========================\n")


def jogar():
    tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 0, 10, 11, 9]

    iniciar_jogo()

    while True:
        mostrar_tabuleiro(tabuleiro)

        if verificar_vitoria(tabuleiro):
            print("Parabéns! Você venceu!")
            break

        movimento = input("Seu movimento: ").lower().strip()

        if movimento == "q":
            print("Jogo encerrado. Até a próxima!")
            break

        elif movimento == "h":
            mostrar_ajuda()
            continue

        elif movimento in ["w", "a", "s", "d"]:
            mover_peca(tabuleiro, movimento)

        else:
            print("Comando desconhecido! Digite H para ver a ajuda.")


if __name__ == "__main__":
    jogar()