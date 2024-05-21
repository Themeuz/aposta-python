# Importância da biblioteca, escolhi random pela ampla versatilidade e documentação, podendo usar também o sorte.py
import random
# Escolhi o time apenas pela dinâmica e futura estética para integração com web-service
import time

# Lista para guardar os números apostados
numero_apostado = []
numero_sorteio = []

# Quantidade de números que podem ser apostados
qtde_numeros = 6

# Recebe e guarda o número de apostas aqui
print("Escolha os números da sua aposta! Precisa escolher de 1 a 62")
while len(numero_apostado) < qtde_numeros:
    try:
        aposta = int(input(f"Escolha o número {len(numero_apostado) + 1}: "))
        if 1 <= aposta <= 62 and aposta not in numero_apostado:
            numero_apostado.append(aposta)
        else:
            print("Número inválido ou já escolhido!")
    except ValueError:
        print("Por favor, insira um número válido.")

print(f"Esta foi a sua aposta: {numero_apostado}")

print("\nAgora vamos ao sorteio!...")

# Realiza o sorteio de números únicos
while len(numero_sorteio) < qtde_numeros:
    sorteio = random.randint(1, 62)
    if sorteio not in numero_sorteio:
        numero_sorteio.append(sorteio)
        time.sleep(1)  # Um segundo para cada número sorteado para aumentar a dinâmica e não ser tão ansioso
        if sorteio in numero_apostado:
            print(f"Sorteio {len(numero_sorteio)}: {sorteio} - ACERTOU!!")
        else:
            print(f"Sorteio {len(numero_sorteio)}: {sorteio} - ERROU!!")

# Contabiliza os acertos
acertos = len(set(numero_apostado) & set(numero_sorteio))
print(f"\nVocê acertou {acertos} números.")
