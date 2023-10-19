temperature = input("enter the temperature: ")
User_temperature = int(temperature)
if User_temperature >= 100:
    print("boiling")
elif 32 < User_temperature < 99:
    print("liquid")
elif User_temperature < 32:
    print("freezing")

