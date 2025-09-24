'Calculadora de dívidas'

dividas = {}
CHAVE = ''
VALOR = 0


while True:
    CHAVE = input('Qual o motivo da dívida? Digite "sair" para sair\n')
    if CHAVE.lower() == 'sair':
        print('-' * 40)
        break
    VALOR = int(input('Qual o valor da dívida?\nR$ '))
    dividas.update({CHAVE.title(): VALOR})
    print(dividas)
    print('-' * 40)

print(dividas)


def calculadora_divida(pendencias):
    "calcular minhas dividas"
    soma_total = 0
    for key, value in pendencias.items():
        print(f'Valor da divida [{key.upper()}]: R$ {value}')
        soma_total += value
    print('-' * 40)
    return soma_total


TOTAL_DIVIDAS = calculadora_divida(dividas)
dias_trabalhados = int(input('Quantos dias você vai trabalhar no mês?\n'))
valor_conta = float(input('Qual o valor em conta?\n'))
media_dia = (TOTAL_DIVIDAS - valor_conta) / dias_trabalhados
print(f'O valor total em dívidas é: R$ {TOTAL_DIVIDAS}\n'
      f'Total em conta: R$ {valor_conta}\n'
      f'Você vai precisar fazer R$ {media_dia:.2f} por dia\n'
      f'para poder pagar sua dívida de R$ {TOTAL_DIVIDAS:.2f} reais\n'
      f'nos {dias_trabalhados} dias que você vai trabalhar\n'
      f'Faltam R${TOTAL_DIVIDAS - valor_conta:.2f} reais para quitar tudo')
