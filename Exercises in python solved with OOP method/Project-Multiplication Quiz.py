class CHRONO:

    def __init__(self):
        import time
        self.value = time.monotonic_ns()

    def game(self, other):
        from random import randint
        import time
        import pyinputplus
        correct = incorrect = int(0)
        while ((self.value - other.value)/1000000000) <= 10:
            if ((self.value - other.value)/1000000000) == 0:
                other.value = time.monotonic_ns()
            n1 = randint(0, 10)
            n2 = randint(0, 10)
            r = pyinputplus.inputInt(f'How much is {n1} x {n2}? ', blank=True)
            self.value = time.monotonic_ns()
            if r == n1 * n2:
                correct += 1
            else:
                incorrect += 1
        return print(f'You aswering {correct} questions correctly and {incorrect} questions incorrectly!')


t = CHRONO()
t0 = CHRONO()
input('After pressing "ENTER" you have 10 seconds to answer as many questions as you can! ')
t.game(t0)
