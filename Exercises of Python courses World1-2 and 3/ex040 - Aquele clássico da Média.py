n1 = float(input('Input the student´s first grade: '))
n2 = float(input('Input the student´s second grade: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('The student have fail!')
elif 5.0 <= m < 7.0:
    print('The student is in recovery!')
elif m >= 7.0:
    print('The student is approved!')
