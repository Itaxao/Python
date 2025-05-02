import random
import os

# Função para limpar a tela (Windows e Linux)
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Função que calcula a pontuação baseando em 100 - tentativas * 5
def calcularPontuacao(tentativas):
    return max(100 - tentativas * 5, 0)

# Função para mostrar o placar ordenado por pontuação
def mostrarPlacar():
    print("\n📋 Placar dos jogadores:")
    if os.path.exists("placar.txt"):
        with open("placar.txt", "r") as arquivo:
            conteudo = arquivo.readlines()

        if conteudo:
            # Ordena o placar pelo valor de pontos (baseado na pontuação, que é o último item da linha)
            placar_ordenado = sorted(conteudo, key=lambda x: int(x.split("|")[-1].split()[1]), reverse=True)

            for linha in placar_ordenado:
                print(linha.strip())
        else:
            print("⚠️ Nenhum placar registrado ainda.")
    else:
        print("⚠️ Nenhum placar encontrado.")

    input("\nPressione ENTER para voltar ao menu...")

# Função principal do jogo
def jogar():
    tentativas = 0
    acertou = False
    limite = 0

    while True:
        dificuldade = input("Selecione a dificuldade\nFácil: 1 a 50\nMédio: 1 a 100\nDifícil: 1 a 200\n→ ").capitalize()

        match dificuldade:
            case "Fácil":
                numeroSorteado = random.randint(1, 50)
                limite = 50
                break
            case "Médio":
                numeroSorteado = random.randint(1, 100)
                limite = 100
                break
            case "Difícil":
                numeroSorteado = random.randint(1, 200)
                limite = 200
                break
            case _:
                print("❌ Opção inválida. Tente novamente.")

    while not acertou:
        try:
            numeroJogador = int(input(f"Digite um valor entre 1 e {limite}: "))
            tentativas += 1

            if numeroJogador < numeroSorteado:
                print("🔺 O número sorteado é maior")
            elif numeroJogador > numeroSorteado:
                print("🔻 O número sorteado é menor")
            else:
                print(f"\n✅ Parabéns! Você acertou o número {numeroSorteado} em {tentativas} tentativas.")
                pontuacao = calcularPontuacao(tentativas)
                print(f"🏆 Sua pontuação: {pontuacao} pontos.")

                nome = input("Digite seu nome para salvar o placar: ")
                with open("placar.txt", "a") as arquivo:
                    arquivo.write(f"{nome} | Dificuldade: {dificuldade} | Número: {numeroSorteado} | Tentativas: {tentativas} | Pontuação: {pontuacao}\n")
                acertou = True
        except ValueError:
            print("⚠️ Por favor, digite um número válido.")

# Menu principal
while True:
    limpar_tela()
    print("🎮 Bem-vindo ao jogo de adivinhação!")
    print("1. Jogar")
    print("2. Ver placar")
    print("3. Sair")
    escolha = input("Escolha uma opção (1/2/3): ")

    if escolha == "1":
        jogar()
    elif escolha == "2":
        mostrarPlacar()
    elif escolha == "3":
        print("👋 Até a próxima!")
        break
    else:
        print("❌ Opção inválida. Tente novamente.")
