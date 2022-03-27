import pyinputplus as py


class PWDTEST:
    def __init__(self, pwd):
        self.pwd = str(pwd)
        self.len = len(pwd)
        if (self.pwd.lower() != self.pwd) and (self.pwd.isalpha() or self.pwd.isalnum()):
            self.upper = True
        else:
            self.upper = False
        if (self.pwd.upper() != self.pwd) and (self.pwd.isalpha() or self.pwd.isalnum()):
            self.lower = True
        else:
            self.lower = False


password = py.inputPassword(prompt='input a password: ', mask='*', limit=None)
passw = PWDTEST(password)
print(passw.pwd, passw.len, passw.upper, passw.lower)
