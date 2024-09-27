# PRINCIPIOS BASICOS DE PYTHON 
# RECEBE OS NUMEROS 10.00 2 5.00 1 30.00
# SAIDA = O preço final do pedido é R$ XX.XX. Seu troco é R$ YY.YY.


import sys
precofinalHamburguer = float()
precofinalBebida = float()
valorfinal = float()
troco = float()
# //Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).
valorHamburguer = float(sys.stdin.readline())
quantidadeHamburguer = int(sys.stdin.readline())
valorBebida = float(sys.stdin.readline())
quantidadeBebida = int(sys.stdin.readline())
precofinalHamburguer = float(quantidadeHamburguer * valorHamburguer)
precofinalBebida = float(quantidadeBebida * valorBebida)
valorfinal = float(precofinalBebida + precofinalHamburguer)
valorPago = float(sys.stdin.readline())
# //Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.
troco = float(valorPago - valorfinal)
# //Imprimir a saída no formato especificado neste desafio.
if troco > 0:
    print(f"O preço final do pedido é R$ {valorfinal:.2f}. Seu troco é R$ {troco:.2f}.")
if troco == 0:
     print(f"O preço final do pedido é R$ {valorfinal:.2f}. Seu troco é R$ {troco:.2f}.")