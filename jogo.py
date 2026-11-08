def iniciar_jogo():
    print("\n" + "=" * 35)
    print("       JOGO DE SEQUÊNCIA")
    print("=" * 35)
    print("Organize os números em ordem crescente!")
    print("Use W, A, S e D para movimentar.")
    print("Digite H para ver a ajuda.")
    print("Digite Q para sair da partida.")
    print("=" * 35)


def criar_tabuleiro(dificuldade):
    if dificuldade == "1":
        linhas = 3
        colunas = 3
        tabuleiro = [
            1, 2, 3,
            4, 0, 6,
            7, 5, 8
        ]

    elif dificuldade == "2":
        linhas = 2
        colunas = 3
        tabuleiro = [
            1, 2, 3,
            0, 4, 5
        ]

    else:
        linhas = 2
        colunas = 2
        tabuleiro = [
            0, 1,
            3, 2
        ]

    return tabuleiro, linhas, colunas


def mostrar_tabuleiro(tabuleiro, colunas):
    print("\n       TABULEIRO")
    print("---------------------")

    for i in range(0, len(tabuleiro), colunas):
        linha = tabuleiro[i:i + colunas]

        print("|", end=" ")

        for numero in linha:
            if numero == 0:
                print("  ", end=" | ")
            else:
                print(f"{numero:2}", end=" | ")

        print("\n---------------------")


def mover_peca(tabuleiro, movimento, linhas, colunas):
    posicao_vazia = tabuleiro.index(0)
    nova_posicao = posicao_vazia

    if movimento == "w":
        if posicao_vazia >= colunas:
            nova_posicao -= colunas
        else:
            print("Movimento inválido! Não há espaço acima.")
            return False

    elif movimento == "s":
        if posicao_vazia < (linhas - 1) * colunas:
            nova_posicao += colunas
        else:
            print("Movimento inválido! Não há espaço abaixo.")
            return False

    elif movimento == "a":
        if posicao_vazia % colunas != 0:
            nova_posicao -= 1
        else:
            print("Movimento inválido! Não há espaço à esquerda.")
            return False

    elif movimento == "d":
        if posicao_vazia % colunas != colunas - 1:
            nova_posicao += 1
        else:
            print("Movimento inválido! Não há espaço à direita.")
            return False

    else:
        print("Comando inválido!")
        return False

    tabuleiro[posicao_vazia], tabuleiro[nova_posicao] = (
        tabuleiro[nova_posicao],
        tabuleiro[posicao_vazia]
    )

    return True


def verificar_vitoria(tabuleiro):
    sequencia_correta = list(range(1, len(tabuleiro))) + [0]
    return tabuleiro == sequencia_correta


def mostrar_ajuda():
    print("\n" + "=" * 30)
    print("             AJUDA")
    print("=" * 30)
    print("W - Mover para cima")
    print("S - Mover para baixo")
    print("A - Mover para a esquerda")
    print("D - Mover para a direita")
    print("H - Mostrar ajuda")
    print("Q - Sair da partida")
    print("=" * 30)


def escolher_dificuldade():
    print("\n========== DIFICULDADE ==========")
    print("1 - Fácil (8 números)")
    print("2 - Normal (5 números)")
    print("3 - Difícil (3 números)")
    print("=================================")

    while True:
        escolha = input("Escolha a dificuldade: ").strip()

        if escolha in ["1", "2", "3"]:
            return escolha

        print("Opção inválida! Escolha 1, 2 ou 3.")


def calcular_medalha(pontos):
    if pontos >= 500:
        return "Ouro"
    elif pontos >= 300:
        return "Prata"
    elif pontos >= 100:
        return "Bronze"
    else:
        return "Sem medalha"


def mostrar_pontuacao(pontos):
    medalha = calcular_medalha(pontos)

    print("\n========== PONTUAÇÃO ==========")
    print(f"Pontos acumulados: {pontos}")
    print(f"Medalha atual: {medalha}")
    print("===============================")


def jogar_partida(dificuldade, pontos):
    tabuleiro, linhas, colunas = criar_tabuleiro(dificuldade)

    if dificuldade == "1":
        nome_dificuldade = "Fácil"
    elif dificuldade == "2":
        nome_dificuldade = "Normal"
    else:
        nome_dificuldade = "Difícil"

    quantidade_movimentos = 0

    iniciar_jogo()

    print(f"\nDificuldade escolhida: {nome_dificuldade}")

    while True:
        mostrar_tabuleiro(tabuleiro, colunas)

        print(f"Movimentos realizados: {quantidade_movimentos}")
        print(f"Pontuação atual: {pontos}")

        if verificar_vitoria(tabuleiro):
            print("\n" + "=" * 35)
            print("       PARABÉNS! VOCÊ VENCEU!")
            print(f"       Movimentos: {quantidade_movimentos}")
            print("       Você ganhou 25 pontos!")
            print("=" * 35)

            return True

        movimento = input("\nEscolha um movimento: ").lower().strip()

        if movimento == "q":
            print("\nPartida encerrada.")
            return False

        elif movimento == "h":
            mostrar_ajuda()

        elif movimento in ["w", "a", "s", "d"]:
            if mover_peca(tabuleiro, movimento, linhas, colunas):
                quantidade_movimentos += 1
                print("Movimento realizado com sucesso!")

        else:
            print("Comando desconhecido! Digite H para ver a ajuda.")


def jogar():
    pontos = 0

    print("\nBem-vindo ao Jogo de Sequência!")

    while True:
        mostrar_pontuacao(pontos)

        dificuldade = escolher_dificuldade()

        venceu = jogar_partida(dificuldade, pontos)

        if venceu:
            pontos += 25
            print("\nSua pontuação foi atualizada!")

        mostrar_pontuacao(pontos)

        resposta = input(
            "\nDeseja jogar outra partida? (s/n): "
        ).lower().strip()

        if resposta != "s":
            print("\nObrigado por jogar!")

            mostrar_pontuacao(pontos)

            print("Até a próxima!")
            break


if __name__ == "__main__":
    jogar()