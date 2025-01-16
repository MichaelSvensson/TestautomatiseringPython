# 3. Använda variabler och datatyper

# 1a
print("Uppgift 1a")
print("----------")
x = input("Ange ett heltal: ")
tal1 = x

# Check if input only consists of digits
if x.isnumeric():
    tal1 = int(x)
    print(tal1)
else:
    print("Endast siffror accepteras!")
print("--------------------------")

# 1b
print("Uppgift 1b")
print("----------")
y = input("Ange ett annat heltal ")
# Check if input only consists of digits
if y.isnumeric():
    tal2 = int(y)
    print(f"tal1+tal2: {tal1+tal2}")
else:
    print("Endast siffror accepteras!")
print("--------------------------")
# 2a
# pris = 2000
# rea_procent = 50
# slut_pris = pris * rea_procent / 100
# print("Att betala ", slut_pris)

# 2b
# pris = 2000
# procent_sats = input("Ange procent-sats (tex: 10) ")
# procent = float(procent_sats)
# rabatt_i_kr = float(pris*(procent/100))
# #print(rabatt_i_kr)
# slut_pris = pris - rabatt_i_kr
# print(procent,"%" + ", som är", rabatt_i_kr, "kr")
# print("Då ska jackan kosta", pris, "-", rabatt_i_kr, "==", slut_pris)





