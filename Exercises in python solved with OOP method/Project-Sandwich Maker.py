import pyinputplus as pyip


class FASTFOOD:
    question = int(0)
    price = int(0)

    def __init__(self, value):
        FASTFOOD.question += 1
        self.value = value
        self.question = FASTFOOD.question

    def sandwich(self):
        if self.question == 1:
            self.value = pyip.inputMenu(self.value, numbered=True)
            if self.value == 'Wheat':
                FASTFOOD.price += float(2.00)
            elif self.value == 'White':
                FASTFOOD.price += float(1.25)
            elif self.value == 'Sourdough':
                FASTFOOD.price += float(2.50)
        elif self.question == 2:
            self.value = pyip.inputMenu(self.value, numbered=True)
            if self.value == 'Chicken':
                FASTFOOD.price += float(2.50)
            elif self.value == 'Turkey':
                FASTFOOD.price += float(3.50)
            elif self.value == 'Ham':
                FASTFOOD.price += float(3.00)
            elif self.value == 'Tofu':
                FASTFOOD.price += float(4.00)
        elif self.question == 3:
            self.value = pyip.inputMenu(self.value, numbered=True)
            if self.value == 'Cheddar':
                FASTFOOD.price += float(0.75)
            elif self.value == 'Swiss':
                FASTFOOD.price += float(1.25)
            elif self.value == 'Mozzarella':
                FASTFOOD.price += float(0.75)
            elif self.value == 'No Cheese':
                self.value = '----'
        elif self.question == 4:
            self.value = 'Yes'
            FASTFOOD.price += float(0.25)
        elif self.question == 5:
            self.value = 'Yes'
            FASTFOOD.price += float(0.25)
        elif self.question == 6:
            self.value = 'Yes'
            FASTFOOD.price += float(0.25)
        elif self.question == 7:
            self.value = 'Yes'
            FASTFOOD.price += float(0.25)
        elif self.question == 8:
            self.value = pyip.inputInt('How many sandwiches do you want? ')
            FASTFOOD.price = FASTFOOD.price * self.value

    def questions(self):
        answer = pyip.inputYesNo(f'Do you want some {self.value}? [Y/N] ')
        if answer == 'yes':
            return self.sandwich()
        else:
            self.value = '----'
            return


# Inputting the variables:
bread = FASTFOOD(['Wheat', 'White', 'Sourdough'])
protein = FASTFOOD(['Chicken', 'Turkey', 'Ham', 'Tofu'])
cheese = FASTFOOD(['Cheddar', 'Swiss', 'Mozzarella', 'No Cheese'])
mayo = FASTFOOD(['Mayo'])
mustard = FASTFOOD(['Mustard'])
lettuce = FASTFOOD(['Lettuce'])
tomato = FASTFOOD(['Tomato'])
number = FASTFOOD(0)
# Choosing ingredients:
bread.sandwich()
protein.sandwich()
cheese.sandwich()
mayo.questions()
mustard.questions()
lettuce.questions()
tomato.questions()
number.sandwich()
# Results:
print(f'Sandwich:\n'
      f'{"Bread:":26} {bread.value:>20}\n'
      f'{"Protein:":26} {protein.value:>20}\n'
      f'{"Cheese:":26} {cheese.value:>20}\n'
      f'{"Mayo:":26} {mayo.value:>20}\n'
      f'{"Mustard:":26} {mustard.value:>20}\n'
      f'{"Lettuce:":26} {lettuce.value:>20}\n'
      f'{"Tomato:":26} {tomato.value:>20}\n'
      f'{"Quantities of sanduíches:":26} {number.value:>20}\n'
      f'{"Total Price:":39} US$ {FASTFOOD.price}')

