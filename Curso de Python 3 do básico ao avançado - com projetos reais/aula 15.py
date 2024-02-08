nome = 'Bruno Hideki Sato Misufara'
altura = 1.80
peso = 72.5
imc = peso / (altura * altura) # IMC = peso / (altura * altura)

# f-strings

linha_1 = f'{nome} tem {altura:.2f} altura'
print(linha_1)

linha_2 = f'pesa {peso} e seu IMC é {imc:.2f}'
print(linha_2)