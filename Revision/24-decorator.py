def perctime(func):
    def wrap(fee, time):
        y = (func(fee, time)/100)
        return (((1+y)**time)-1)*100
    return wrap


@perctime
def yeartomonth(fee, time):
    x = fee/100
    return (((1+x)**(1/12))-1) * 100


fees = float(input("Enter the percentage fee per year: "))
time = int(input("How many months this percentage will be applied? "))
print(f"The total amount of percentage applied in {time} months will be {yeartomonth(fees, time):.3}%")

