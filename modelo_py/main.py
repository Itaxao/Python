# Função que calcula as operações
def calcular_operacoes(a,b):
    """ CALCULA E RETORNA AS 6 OPERACOES PRINCIPAIS"""
    # Array para armazenar as operacoes
    resultados = {
        'soma': a+b,
        'subtracao':a-b,
        'multiplicacao':a*b,
        'divisao':a/b if b != 0 else "Erro: Divisão por zero",
        'resto': a%b if b!= 0 else "Erro: Divisão por zero",
        'potencia': a**b
    }
    return resultados

# Função que exibe os resultados
def exibir_resultados(a,b,operacoes):
    """Exibe os resultados formatados das operações."""
    print(f"\n→ Resultados para {a} e {b}:")
    print(f" {'SOMA:':<15} → {a} + {b} = {operacoes['soma']}.")
    print(f" {'SUBTRACAO:':<15} → {a} - {b} = {operacoes['subtracao']}.")
    print(f" {'MULTPLICACAO:':<15} → {a} * {b} = {operacoes['multiplicacao']}.")
    print(f" {'DIVISAO:':<15} → {a} / {b} = {operacoes['divisao']}.")
    print(f" {'RESTO:':<15} → {a} % {b} = {operacoes['resto']}.")
    print(f" {'POTENCIA:':<15} → {a} ^ {b} = {operacoes['potencia']}.")

# Função que obtêm os valores
def obter_numeros():
    """Solicita e retorna dois números inteiros ao usuário."""
    # Loop até receber entrada válida (evita recursão)
    while True:

        # Garante que o valor será inteiro
        try:
            a = float(input("Digite um valor real: "))
            b = float(input("Digite outro valor real: "))
            return a,b
        
        # Caso não seja, retorna erro 
        except ValueError:
            print("Por favor, digite um valor valido!")


# Garante que o código só execute se o arquivo for rodado diretamente
if __name__ == "__main__":
    print("🌟 Calculadora 4 Operações 🌟")
    a,b = obter_numeros()
    operacoes = calcular_operacoes(a,b)
    exibir_resultados(a,b,operacoes)