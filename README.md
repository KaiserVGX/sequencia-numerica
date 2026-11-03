# Jogo de Sequência Numérica

## Sobre o projeto

### Este projeto consiste em um jogo de sequência numérica desenvolvido em Python, executado pelo terminal.

O objetivo do jogo é organizar os números em ordem crescente, utilizando o espaço vazio para movimentar as peças.

O projeto foi desenvolvido como atividade acadêmica para praticar lógica de programação, funções, listas, estruturas condicionais e estruturas de repetição.

Objetivo do jogo

O tabuleiro possui 12 espaços organizados em 4 linhas e 3 colunas. Onze espaços contêm números e um espaço permanece vazio.

O objetivo é organizar os números de 1 a 11 em ordem crescente, deixando o espaço vazio na última posição.

Exemplo do tabuleiro organizado:

1 |  2 |  3
4 |  5 |  6
7 |  8 |  9

10 | 11 |

Requisitos

Para executar o projeto, é necessário ter o Python 3 instalado no computador.

Não são necessárias bibliotecas externas.

Como executar

1. Baixe ou clone o repositório.

2. Abra o terminal na pasta do projeto.

3. Execute o comando:
   
   python3 jogo.py

No Windows, também pode ser possível executar com:

   python jogo.py

Comandos do jogo

Tecla| Função
W| Move o espaço vazio para cima
S| Move o espaço vazio para baixo
A| Move o espaço vazio para a esquerda
D| Move o espaço vazio para a direita
H| Exibe a ajuda
Q| Encerra a partida

Movimentos inválidos são rejeitados pelo jogo.

Ao encerrar uma partida, o jogador pode escolher se deseja jogar novamente.

Funcionalidades

- Exibição do tabuleiro numérico.
- Movimentação das peças.
- Validação dos movimentos.
- Verificação da condição de vitória.
- Contagem dos movimentos realizados.
- Exibição de instruções durante o jogo.
- Opção para encerrar a partida.
- Opção para reiniciar a partida.

Tecnologias utilizadas

- Python 3
- Git
- GitHub

Organização do projeto

sequencia-numerica/
├── jogo.py
└── README.md

Autores

Projeto desenvolvido em colaboração por Lucas e Rafael, como atividade acadêmica da disciplina Lógica de Programação.

Observação

O tabuleiro começa em uma configuração inicial fixa. O jogo não utiliza embaralhamento aleatório.