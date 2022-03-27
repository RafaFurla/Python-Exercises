class PWDTEST:
    def __init__(self, pwd):
        self.stg = str('')
# PASSWORD
        self.pwd = str(pwd)
# LENGTH
        if len(pwd) >= 8:
            self.len = True
        else:
            self.len = False
            self.stg += '<Try at least 8 characters>'
# UPPER
        if (self.pwd.lower() != self.pwd) and (self.pwd.isalpha() or self.pwd.isalnum()):
            self.upper = True
        else:
            self.upper = False
            self.stg += '<Try to put some upper characters>'
# LOWER
        if (self.pwd.upper() != self.pwd) and (self.pwd.isalpha() or self.pwd.isalnum()):
            self.lower = True
        else:
            self.lower = False
            self.stg += '<Try to put some lower characters>'
# ALPHANUMERIC
        if ("0" in self.pwd) or ("1" in self.pwd) or ("2" in self.pwd) or ("3" in self.pwd) or ("4" in self.pwd) or \
                ("5" in self.pwd) or ("6" in self.pwd) or ("7" in self.pwd) or ("8" in self.pwd) or ("9" in self.pwd):
            self.alnum = True
        else:
            self.alnum = False
            self.stg += '<Try to mix numbers and alphabetic characters>'
# STRENGHT
        if self.stg == '':
            self.power = 'Strong password'
        else:
            self.power = 'Weak password'

    def result(self):
        return f"{'Password:':33}'{self.pwd}'\n{'Has password a security length?':33}{self.len}\n{'Have password upper characters?':33}{self.upper}\n{'Have password lower characters?':33}{self.lower}\n{'Is password alphanumeric?':33}{self.alnum}\n{'Is password weak or strong?':33}{self.power}\n{'Notes:':33}{self.stg}"


password = PWDTEST(str(input('Input a password: ')))
print(password.result())
