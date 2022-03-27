class WORDS:
    def __init__(self, mean):
        self.mean = str(mean)

    def striping(self):
        if self.mean.count(' ') > 0:
            self.mean = self.mean.split()
            self.mean = ' '.join(self.mean)


write = WORDS(input('Input a String: '))
write.striping()
print(write.mean)
