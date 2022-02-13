# Calcula o novo salário de um funcionário depois de um reajuste de mais 15%
s = float(input('Qual o seu salário atual? R$ '))
ns = s + (s * 0.15)
print('O salário foi reajustado em mais 15% ({:.2f} reais) e agora passou a ser {:.2f} reais'.format(s * 0.15, ns))
