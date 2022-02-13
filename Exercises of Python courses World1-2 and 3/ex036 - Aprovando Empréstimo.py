color = {'clean': '\033[m', 'red': '\033[31m', 'white': '\033[1;97m', 'green': '\033[32m'}
print(color['red'], '=+=' * 22, color['clean'])
print(color['white'], ' This program calculates the cost of financing and it´s viability')
print(color['red'], '=+=' * 22, color['clean'])
price = float(input('What´s the property price? (in R$) '))
income = float(input('How much is your income? (in R$) '))
time = int(input('How many months do you need to pay the financing? '))
parcel = price/time
if parcel > income * 0.3:
    print('{}Unfortunately you can´t acquire the financing!\n' 
          'The parcel by month is R$ {:.2f} and it´s more than 30% if your incomes!'
          .format(color['red'], parcel))
else:
    print('{}Congratulations you acquire the financing! \n'
          'The parcel by month is R$ {:.2f}'.format(color['green'], parcel))
