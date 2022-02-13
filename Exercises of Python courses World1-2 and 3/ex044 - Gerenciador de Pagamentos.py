print('{:*^75}'.format('LOJAS GUANABARA'))  # Essa linha de comando serve para centralizar o texto que se queira colocar.
print('=+=' * 25)
print(' This software calculates the price accordingly with the method of payment')
print('=+=' * 25)
price = float(input('What is the price of the product? US$ '))
print('')
paymethod = int(input('''              CHOOSE THE PAYMENT METHOD 
[1] Money or Check: this generates 10% of discount
[2] 1x in credit card: this generates 5% of discount
[3] 2x in credit card: this don´t generates discount
[4] 3x or more in credit card: insides 20% of fees
Select one option represented by one of the numbers above: '''))
if paymethod == 1:
    print('The final price is: US$ {:.2f}'.format(price * 0.90))
elif paymethod == 2:
    print('The final price is: US$ {:.2f}'.format(price * 0.95))
elif paymethod == 3:
    print('The final price is: US$ {:.2f}'.format(price))
elif paymethod == 4:
    print('The final price is: US$ {:.2f}'.format(price * 1.2))
else:
    print('{} is not a valid option! Choose between [1], [2], [3] or [4]'.format(paymethod))
