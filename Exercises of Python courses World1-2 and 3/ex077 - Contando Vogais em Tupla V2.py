tupla = (str(input('Escreva uma palavra: ')).strip(), str(input('Escreva outra palavra: ')).strip(),
         str(input('Escreva mais uma palavra: ')).strip(), str(input('Escreva a última palavra: ')).strip())
for palavra in tupla:
    print(f'Na palavra {palavra.upper()} temos as seguintes vogais: ', end='')
    for letra in palavra:
         if letra in 'aáàâãäeéèêëiíìîïoóòôõöuúùûüAÁÀÂÃÄEÉÈÊËIÍÌÎÏOÓÒÔÕÖUÚÙÛÜ':
              print(letra.lower(), end=' ')
    print()
