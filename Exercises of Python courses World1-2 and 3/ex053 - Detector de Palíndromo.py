# tirando os espaços à esquerda e à direita e passando todas as letras da frase para minúsculas:
#frase = str(input('Digite uma frase: ')).strip().lower()
# tirando a pontuação e espaços da frase:
#frase = frase.replace('.', '')
#frase = frase.replace(',', '')
#frase = frase.replace(';', '')
#frase = frase.replace(':', '')
#frase = frase.replace('/', '')
#frase = frase.replace('?', '')
#frase = frase.replace('!', '')
#frase = frase.replace(' ', '')
#frase = frase.replace('á', 'a')
#frase = frase.replace('é', 'e')
#frase = frase.replace('í', 'i')
#frase = frase.replace('ó', 'o')
#frase = frase.replace('ú', 'u')
#frase = frase.replace('ã', 'a')
#frase = frase.replace('õ', 'o')
#frase = frase.replace('â', 'a')
#frase = frase.replace('ê', 'e')
#frase = frase.replace('î', 'i')
#frase = frase.replace('ô', 'o')
#frase = frase.replace('û', 'u')
#frase = frase.replace('à', 'a')
#if frase == frase[len(frase)::-1]:  # isso aqui (::1) só funciona no python, em outras linguagens não!
#    print('A frase digitada é um políndromo! Isto é, se escrita de trás para frente'
#          ' é igual a ela escrita de frente para trás!')
#else:
#    print('A frase digitada não é um políndromo.')
# Exemplos de políndronos: Apos a sopa / A sacada da casa / A torre da derrota / O lobo ama o bolo /
# anotaram a data da maratona

# Outra forma de fazer:
frase1 = str(input('Digite uma frase: ')).strip().lower()
frase1 = frase1.replace('.', '')
frase1 = frase1.replace(',', '')
frase1 = frase1.replace(';', '')
frase1 = frase1.replace(':', '')
frase1 = frase1.replace('/', '')
frase1 = frase1.replace('?', '')
frase1 = frase1.replace('!', '')
frase1 = frase1.replace(' ', '')
frase1 = frase1.replace('á', 'a')
frase1 = frase1.replace('é', 'e')
frase1 = frase1.replace('í', 'i')
frase1 = frase1.replace('ó', 'o')
frase1 = frase1.replace('ú', 'u')
frase1 = frase1.replace('ã', 'a')
frase1 = frase1.replace('õ', 'o')
frase1 = frase1.replace('â', 'a')
frase1 = frase1.replace('ê', 'e')
frase1 = frase1.replace('î', 'i')
frase1 = frase1.replace('ô', 'o')
frase1 = frase1.replace('û', 'u')
frase1 = frase1.replace('à', 'a')
inverso = str('')
for c in range(len(frase1) - 1, -1, -1):
    inverso += frase1[c]
if frase1 == inverso:
    print('''Temos um palíndromo. A frase digitada foi: {} 
                           e a invertida é {}'''.format(frase1, inverso))
else:
    print('''A frase digitada não é um palíndromo. Frase digitada: {}.
                                     Frase invertida: {}'''.format(frase1, inverso))
