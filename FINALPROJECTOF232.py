def compound_interest(initial, rate, time):
    Amount = initial * (pow((1 + rate / 100), time))
    final = Amount - initial
    return final


print("Welcome to our compound interest calculator program for BUS232")
inital = int(input("Plase enter the initial amount: "))
rate = int(input("Please enter the intereset rate: "))
time = float(input("Plase enter the time: "))

final = compound_interest(inital,rate,time)

print(final)

print("Compound Interest is :",final)
choice = int(input("Would you like to save the output to a txt file? Yes (1) No (2)"))
if choice == 1:
    f = open("Compound_Interest_Output.txt", "a")
    print("Compound Interest is: ",final," for initial:",inital," rate: ",rate,"time: ",time,file=f)
    print("Output is save to file")
