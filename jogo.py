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