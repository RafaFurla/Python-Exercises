from random import randint
set1 = set()
set2 = set()
for c in range (1, 10, 1):
    set1.add(randint(1, 20))
    set2.add(randint(1, 20))
print(f"set1 = {set1}\nset2 = {set2}")
print(f"set1 union set2 = {set1 | set2}")
print(f"set1 intersection set2 = {set1 & set2}")
print(f"set1 difference set2 = {set1 - set2}")
print(f"set2 difference set1 = {set2 - set1}")
print(f"set1 symmetric difference set2 = {set1 ^ set2}")

