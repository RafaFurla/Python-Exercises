word = str(input('Input something: '))
print('The primitive type of this value is: {}'.format(word.__class__))
print('The primitive type of this value is: ', type(word))  # another way to do the same thing
print('Only have spaces? {}'.format(word.isspace()))
print('Is it a number? {}'.format(word.isnumeric()))  # accept characters of the type: ½, ¼, ¹, ², ³
print('Is it decimal? {}'.format(word.isdecimal()))  # just accept numbers on the standard keybord: 1, 2, 3, 4,
# 5, 6, 7, 8, 9, 0
print('Is it just formed by digits? {}'.format(word.isdigit()))  # accept characters of the type: ¹, ², ³
print('Is alphabetic? {}'.format(word.isalpha()))
print('Is alphanumeric? {}'.format(word.isalnum()))
print('Is it all capitalcases? {}'.format(word.isupper()))
print('Is it all lowercases? {}'.format(word.islower()))
print('Is it capitalize? {}'.format(word.istitle()))
