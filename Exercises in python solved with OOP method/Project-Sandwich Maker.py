import pyinputplus as pyip


class FASTFOOD:
    question = int(0)

    def __init__(self, value):
        FASTFOOD.question += 1
        self.value = value
        self.question = FASTFOOD.question

    def sandwich(self):
        if self.question == 1:
            self.value = pyip.inputMenu(self.value, numbered=True)
        elif self.question == 2:
            self.value = pyip.inputMenu(self.value, numbered=True)
        elif self.question == 3:
            self.value = pyip.inputMenu(self.value, numbered=True)
        elif self.question == 4:
            self.value = pyip.inputMenu(self.value, numbered=True)
        elif self.question == 5:
            self.value = pyip.inputInt('How many sandwiches do you want? ')


bread = FASTFOOD(['Wheat', 'White', 'Sourdough'])
protein = FASTFOOD(['Chicken', 'Turkey', 'Ham', 'Tofu'])
cheese = FASTFOOD(['Cheddar', 'Swiss', 'Mozzarella'])
sauce = FASTFOOD(['Mayo', 'Mustard', 'Lettuce', 'Tomato'])
number = FASTFOOD(0)
bread.sandwich()
protein.sandwich()
r = pyip.inputYesNo('Do you want some cheese? ')
if r == 'yes':
    cheese.sandwich()
else:
    cheese.value = ''
sauce.sandwich()
number.sandwich()

if cheese.value == '':
    print(f'Sandwich:\nBread: {bread.value}\nProtein: {protein.value}\nSauce: {sauce.value}\nQuantaties of sanduíches: {number.value}')
else:
    print(f'Sandwich:\nBread: {bread.value}\nProtein: {protein.value}\nCheese: {cheese.value}\nSauce: {sauce.value}\nQuantaties of sanduíches: {number.value}')
