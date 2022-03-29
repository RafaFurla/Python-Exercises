class PWDTEST:
    def __init__(self, pwd, len_, upper, lower, alnum, stg):
        self.pwd = pwd
        self.len_ = len_
        self.upper = upper
        self.lower = lower
        self.alnum = alnum
        self.stg = stg

    @classmethod
    def testing(cls, pwd):
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
        if not pwd.isnumeric() and not pwd.isalpha():
            alnum = True
        else:
            alnum = False
            stg += '<Try to mix numbers and alphabetic characters>'
        # STRENGHT
        if stg == '':
            return cls(pwd, len_, upper, lower, alnum, stg)
        else:
            return print(f"Weak password: {stg}")

    def get_result(self):
        return f"{'Password:':33}'{self.pwd}'\n{'Has password a security length?':33}{self.len_}\n" \
               f"{'Has password upper characters?':33}{self.upper}\n{'Has password lower characters?':33}" \
               f"{self.lower}\n{'Is password alphanumeric?':33}{self.alnum}\n{'Notes:':33}" \
               f"{'The password is strong and was add successfully'}"

    @property
    def changepass(self):
        return self.get_result()

    @changepass.setter
    def changepass(self, pwd):
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
        if not pwd.isnumeric() and not pwd.isalpha():
            alnum = True
        else:
            alnum = False
            stg += '<Try to mix numbers and alphabetic characters>'
        # STRENGHT
        if stg == '':
            PWDTEST(pwd, len_, upper, lower, alnum, stg)
        else:
            print(f"Weak password: {stg}")


while True:
    password = PWDTEST.testing(str(input('Input a password: ')))
    if password is None:
        print('Try again!')
    else:
        print(password.changepass)
        break

r = password.changepass = str(input('Change your password: '))
print(r)
print(password.pwd)

while True:
    password.changepass = str(input('Change your password: '))
    if password is None:
        print('Try again!')
    else:
        print(password.changepass)
        break
