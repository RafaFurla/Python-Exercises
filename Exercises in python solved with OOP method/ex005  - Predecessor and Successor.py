class PHRASE:
    def __init__(self, message, color='blue'):
        self.message = str(message)
        self.color = str(color)
        if self.color == 'red':
            self.message = '\033[31m' + self.message + '\033[m'
        elif self.color == 'green':
            self.message = '\033[32m' + self.message + '\033[m'
        elif self.color == 'yellow':
            self.message = '\033[33m' + self.message + '\033[m'
        elif self.color == 'violet':
            self.message = '\033[35m' + self.message + '\033[m'
        elif self.color == 'blue':
            self.message = '\033[36m' + self.message + '\033[m'

    def prt(self):
        return f"\033[35m{'#' * len(self.message)}\033[m\n{self.message:^{len(self.message) + 8}}\n\033[35m{'#' * len(self.message)}\033[m"


class PREDSUC:
    def __init__(self, value):
        self.value = int(value)

    def pred(self):
        return self.value - 1

    def suc(self):
        return self.value + 1


msg = PHRASE('An Script that print the predecessor and the successor of the input number', 'blue')
print(msg.prt())
num = PREDSUC(input('Input a Integer Number: '))
print(f"The predecessor of number \033[32m{num.value}\033[m is the number \033[33m{num.pred()}\033[m and the sucessor is number \033[31m{num.suc()}\033[m")

