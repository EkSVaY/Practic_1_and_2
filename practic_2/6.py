# Task_6_Ekin_Viacheslaw

mass_kg = (float(input("Введите вес в фунтах: ")) * 0.4535)
height_cm = (float(input("Введите рост в дюймах: ")) * 2.54)
imt = mass_kg / ((height_cm / 100) ** 2)

print(imt)
