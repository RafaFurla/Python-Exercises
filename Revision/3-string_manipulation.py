a = input("Type anything you want: ")

print(f'Is user typed a number? {a.isnumeric()}')

print(f'Is user typed only letters? {a.isalpha()}')

print(f'Is user typed an alphanumerical sentence? {a.isalnum()}')

print(f'Is user typed a capital sentence? {a.isupper()}')

print(f'Is user typed a lowercase sentence?  {a.islower()}')

print(f'Is user typed something that could be printed? {a.isprintable()}')

print(f'Is user typed a title sentence? {a.istitle()}')

print(f'The user typed {len(a)} characters')

print(f"The user typed {a.count('o')} times the letter O")

print(f'The word "Rafa" is located in the position: {a.find("Rafa")}')

print(f"Is the expression 'afa' located in what user typed? {'afa' in a}")

print("Now we will replace the 'el' for 'ela' in the sentence typed by the user.")
b = a.replace("el", "ela")
print(f"After the substitution, the sentence typed by the user stays: {b}")

print("Now we will put everything typed by the user in capital characters.")
b = a.upper()
print(f"The result is: {b}")

print("Now we will put in lowercase every character typed by the user.")
b = a.lower()
print(f"The result is: {b}")

print("Now we will titled the user's first word of the sentense.")
b = a.capitalize()
print(f"The result is: {b}")

print(f"Now we will title the entire sentence that user typed.")
b = a.title()
print(f"The result is: {b}")

print("Now we will remove spaces before and after the sentence typed by the user.")
b = a.strip()
print(f"The result is: {b}")

print("Let's strip the spaces in the right site of the sentence.")
b = a.rstrip()
print(f"The result is: {b}")

print("Let's strip the spaces in the left site of the sentence.")
b = a.lstrip()
print(f"The result is: {b}")

print("Let's split the sentence in the spaces between the words.")
b = a.strip().split()
print(f"The result is: {b}")

print("Now let's put together the last result in a unic sentence again.")
b = ' '.join([b[0], b[1], b[2]])
print(f"The result is: {b}")

print(f"Is the first word of the sentence 'Rafael'? {a.startswith('Rafael')}")

print(f"Is the last word of the sentence 'Furlanetto'? {a.endswith('Furlanetto')}")

print(f"Printing the sentence from the first character to the seventh character: {a[0:6:1]}")

print(f"Printing the sentence from the seventh character to the first character. Jumping 2 by 2 characters at each time: {a[6:0:-2]}")
