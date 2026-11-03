def iniciar_jogo():
    print("\n" + "=" * 35)
    print("       JOGO DE SEQUÊNCIA")
    print("=" * 35)
    print("Organize os números em ordem crescente!")
    print("W - Mover para cima")
    print("S - Mover para baixo")
    print("A - Mover para a esquerda")
    print("D - Mover para a direita")
    print("H - Mostrar ajuda")
    print("Q - Sair do jogo")
    print("=" * 35)


def mostrar_tabuleiro(tabuleiro):
    print("\n       TABULEIRO")
    print("---------------------")

    for i in range(0, len(tabuleiro), 3):
        linha = tabuleiro[i:i + 3]

        print("|", end=" ")

        for numero in linha:
            if numero == 0:
                print("  ", end=" | ")
            else:
                print(f"{numero:2}", end=" | ")

        print("\n---------------------")


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
        tabuleiro[posicao_vazia]
    )

    return True


def verificar_vitoria(tabuleiro):
    sequencia_correta = list(range(1, 12)) + [0]
    return tabuleiro == sequencia_correta


def criar_tabuleiro():
    return [
        1, 2, 3,
        4, 5, 6,
        7, 8, 0,
        10, 11, 9
    ]


def mostrar_ajuda():
    print("\n" + "=" * 30)
    print("             AJUDA")
    print("=" * 30)
    print("W - Mover para cima")
    print("S - Mover para baixo")
    print("A - Mover para a esquerda")
    print("D - Mover para a direita")
    print("H - Mostrar esta ajuda")
    print("Q - Encerrar o jogo")
    print("=" * 30)


def testar_movimentacao():
    tabuleiro = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 0,
        10, 11, 9
    ]

    assert mover_peca(tabuleiro, "a") is True
    assert tabuleiro == [
        1, 2, 3,
        4, 5, 6,
        7, 0, 8,
        10, 11, 9
    ]

    print("Teste de movimentação: OK")


def testar_movimento_invalido():
    tabuleiro = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 0,
        10, 11, 9
    ]

    tabuleiro_original = tabuleiro.copy()

    resultado = mover_peca(tabuleiro, "d")

    assert resultado is False
    assert tabuleiro == tabuleiro_original

    print("Teste de movimento inválido: OK")


def testar_vitoria():
    tabuleiro_correto = list(range(1, 12)) + [0]

    assert verificar_vitoria(tabuleiro_correto) is True

    print("Teste de vitória: OK")


def executar_testes():
    print("\nExecutando testes do jogo...\n")

    testar_movimentacao()
    testar_movimento_invalido()
    testar_vitoria()

    print("\nTodos os testes foram concluídos com sucesso!")


def jogar():
    tabuleiro = criar_tabuleiro()
    quantidade_movimentos = 0

    iniciar_jogo()

    while True:
        mostrar_tabuleiro(tabuleiro)

        print(f"Movimentos realizados: {quantidade_movimentos}")

        if verificar_vitoria(tabuleiro):
            print("\n" + "=" * 35)
            print("       PARABÉNS! VOCÊ VENCEU!")
            print(f"       Total de movimentos: {quantidade_movimentos}")
            print("=" * 35)
            break

        movimento = input("\nEscolha um movimento: ").lower().strip()

        if movimento == "q":
            print("\nJogo encerrado. Até a próxima!")
            break

        elif movimento == "h":
            mostrar_ajuda()

        elif movimento in ["w", "a", "s", "d"]:
            if mover_peca(tabuleiro, movimento):
                quantidade_movimentos += 1
                print("Movimento realizado com sucesso!")

        else:
            print("Comando desconhecido! Digite H para ver a ajuda.")


if __name__ == "__main__":
    executar_testes()

    jogar()