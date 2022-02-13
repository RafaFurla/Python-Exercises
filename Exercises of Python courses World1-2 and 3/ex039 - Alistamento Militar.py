from datetime import date
d = int(input('In what day did you birth? '))
m = int(input('In what month did you birth? '))
y = int(input('In what year did you birth? '))
td = date.today().day
tm = date.today().month
ty = date.today().year
if ty < y+18:
    difm = (12 - tm + m) / 12
    dif = (y+18-1-ty+difm) // 1
    print(dif)
    print('Você ainda terá que se alistar no serviço militar! Falta(m) ', dif, ' ano(s) e {:.1f} mes(es)'
          .format((difm - (difm // 1)) * 12))
if ty > y+18:
    difm = (12 - m + tm) / 12
    dif = ((ty-1)-(y+18)+difm) // 1
    print('Passaram-se ', dif, ' ano(s) e {:.1f} mes(es) do seu alistamento militar obrigatório!'
          .format((difm - (difm // 1)) * 12))
if ty == y+18:
    if tm < m:
        difm = (m - tm)
        print('Você ainda terá que se alistar no serviço militar! Faltam ', difm, ' mes(es)')
    if tm > m:
        difm = (tm - m)
        print('Já se passou ', difm, ' mes(es) do seu tempo de alistamento!')
    if tm == m:
        if td < d:
            print('Você ainda terá que se alistar no serviço militar! Faltam: ', d - td, 'dia(s)')
        if td > d:
            print('Já se passou ', td - d, ' dia(s) do seu tempo de alistamento!')
        if td == d:
            print('Hora de se alistar!')
