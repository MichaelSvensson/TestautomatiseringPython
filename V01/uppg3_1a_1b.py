# 3. Använda variabler och datatyper

# 1a
print("Uppgift 1a")
print("----------")
x = input("Ange ett heltal: ")
tal1 = x

# Check if input only consists of digits and no float-number
if x.isnumeric():
    tal1 = int(x)
    print(tal1)
else:
    print("Endast heltal accepteras!")
    exit()
print("--------------------------")


# 1b
print("Uppgift 1b")
print("----------")
y = input("Ange ett annat heltal ")
# Check if input only consists of digits and no float-number
if y.isnumeric():
    tal2 = int(y)
    print(f"tal1+tal2: {tal1+tal2}")
else:
    print("Endast heltal accepteras!")
print("--------------------------")





