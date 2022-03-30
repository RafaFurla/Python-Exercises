try:
    file = open(r"C:\Users\rafaf\Desktop\teste\Hello World.txt")
    cont = file.read()
    print(cont)
    print(1/0)
except (ZeroDivisionError, FileNotFoundError):
    print('Passed by except')
finally:
    try:
        file.close()
        print('Passed by finally')
    except (FileNotFoundError, NameError):
        print('Passed by second except')
    finally:
        print('End of program!')

with open(r"C:\Users\rafaf\Desktop\teste\Hello World.txt") as f:
    print(f.read())
