print('This software uses the measure of 3 half-lines to see if they form '
      'a triangle and what tipo of triangle they form!')
l1 = float(input('Input the first half-line measure: '))
l2: float = float(input('Input the second half-line measure: '))
l3 = float(input('Input the third half-line measure: '))
if ((l2 - l3) ** 2) ** (1 / 2) < l1 < l2 + l3 and ((l1 - l3) ** 2) ** (1 / 2) < l2 < l1 + l3 \
        and ((l1 - l2) ** 2) ** (1 / 2) < l3 < l1 + l2:
    if l1 == l2 == l3:
        print('The half-lines forms a triangle and it is equilateral!')
    if l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l2 == l3 and l2 != l1:
        print('The half-lines forms a triangle and it is isosceles!')
    if l1 != l2 != l3 != l1:
        print('The half-lines forms a triangle and it is scalene!')
else:
    print('The half-lines don´t forms a triangle!')
