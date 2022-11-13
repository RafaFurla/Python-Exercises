print("="*30)
print("Select:")
print("1 - If your car goes straight")
print("2 - If your car turn left")
print("3 - If your car turn right")
print("4 - If your car reverses")
print("="*30)
a = int(input("Enter with your choose: "))
if a == 1:
    print("Your car goes straight!")
elif a == 2:
    print("Your car turn left")
elif a == 3:
    print("Your car turn right")
elif a == 4:
    print("Your car reverses")
else: 
    print("You don't choose a valid option!")

