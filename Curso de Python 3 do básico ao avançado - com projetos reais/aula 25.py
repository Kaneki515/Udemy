# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia 
# toda a expressão como verdadeira
# Se qualquer valor for considerado verdadeiro,
# a expresão inteira será avaliada naquele valor.
# São considerados falsy
# 0 0.0 '' False
# usado para representar um não valor 

# entrada = input('[E] = Entrar || [S] = Sair: ')
# senha = input('Senha: ')

# senha_permitida = '123'

# if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
#   print('Entrar')
# else:
#   print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
