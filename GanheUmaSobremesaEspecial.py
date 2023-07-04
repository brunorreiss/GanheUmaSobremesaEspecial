import sys

valorPedido = float(sys.stdin.readline())

if valorPedido >= 50.0:
    mensagem = "Parabens, você ganhou uma sobremesa gratis!"
else:
    mensagem = "Que pena, você nao ganhou nenhum brinde especial."

print(mensagem)
