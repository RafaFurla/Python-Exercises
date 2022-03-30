file = open(r'C:\Users\rafaf\Desktop\Books.txt', 'r')

bk = []
name = str('')
for line in file.readlines():
    book = line.split()
    for c in book:
        name += c[0]
    bk.append(name)
    name = str('')
    del book
for line in bk:
    print(line)
file.close()
