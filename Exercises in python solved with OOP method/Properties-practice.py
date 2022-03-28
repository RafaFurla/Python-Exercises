class PWDTEST:
    def __init__(self, pwd, len_, upper, lower, alnum, stg):
        self.pwd = pwd
        self.len_ = len_
        self.upper = upper
        self.lower = lower
        self.alnum = alnum
        self.stg = stg

    @classmethod
    def _testing(cls, pwd):
        stg = str('')
        # LENGTH
        len_ = len(pwd)
        if len_ >= 8:
            len_ = True
        else:
            len_ = False
            stg += '<Try at least 8 characters>'
        # UPPER
        if (pwd.lower() != pwd) and (pwd.isalpha() or pwd.isalnum()):
            upper = True
        else:
            upper = False
            stg += '<Try to put some upper characters>'
        # LOWER
        if (pwd.upper() != pwd) and (pwd.isalpha() or pwd.isalnum()):
            lower = True
        else:
            lower = False
            stg += '<Try to put some lower characters>'
        # ALPHANUMERIC
        if ("0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9") in pwd:
            alnum = True
        else:
            alnum = False
            stg += '<Try to mix numbers and alphabetic characters>'
        # STRENGHT
        if stg == '':
            return cls(pwd, len_, upper, lower, alnum, stg)
        else:
            return print(f"Weak password: {stg}")

    def result(self):
        return f"{'Password:':33}'{self.pwd}'\n{'Has password a security length?':33}{self.len_}\n{'Has password upper characters?':33}{self.upper}\n{'Has password lower characters?':33}{self.lower}\n{'Is password alphanumeric?':33}{self.alnum}\n{'Notes:':33}{'The password is strong and was add successfully'}"

    def set_changepass(self, pwd):
        return PWDTEST._testing(pwd)


while True:
    password = PWDTEST._testing(str(input('Input a password: ')))
    if password is None:
        print('Try again!')
    else:
        print(password.result())
        break

while True:
    password.set_changepass(str(input('Input your new password: ')))
    if password is None:
        print('Try again!')
    else:
        print(password.result())
        break
print(PWDTEST.__dict__)
