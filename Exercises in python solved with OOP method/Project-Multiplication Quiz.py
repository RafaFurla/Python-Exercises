from random import randint
import time




correct = incorrect = 0
input('You have 10 seconds after pressing enter to answer as many questions as you can! ')
now = time.time()
future = now + 10
for c in range(0, 50):
    while time.time() < future:
        n1 = randint(0, 10)
        n2 = randint(0, 10)
        r = int(input(f'How much is {n1} x {n2}? '))
        if r == n1 * n2:
            correct += 1
        else:
            incorrect += 1
print(f'You aswering {correct} questions correctly and {incorrect} questions incorrectly!')
