from random import randint
import time
input('After pressing "ENTER" you have 10 seconds to answer as many questions as you can! ')
correct = incorrect = int(0)
t0 = time.monotonic_ns()
t = time.monotonic_ns()
while ((t - t0)/1000000000) < 10:
    if ((t - t0)/1000000000) == 0:
        t0 = time.monotonic_ns()
    n1 = randint(0, 10)
    n2 = randint(0, 10)
    r = int(input(f'How much is {n1} x {n2}? '))
    t = time.monotonic_ns()
    if r == n1 * n2:
        correct += 1
    else:
        incorrect += 1
print(f'You aswering {correct} questions correctly and {incorrect} questions incorrectly!')

