# Uppgift - Balder
# 2
# 1.	Fråga användaren hur lång man är (i cm)
# 2.	Skriv ut antingen "Du får åka!" eller "Du får inte åka"
# Skriv in följande värden för att testa att ditt program gjort rätt:
# A.	121 cm (får inte åka)
# B.	130 cm (får åka)
# C.	155 cm (får åka)

print("För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!")
x = input("Hur lång är är ni i cm: ")
if x.isnumeric():
    length = float(x)
    if length < 130:
        print("Du får inte åka!")
    else:
        print("Du får åka!")

else:
    print("Endast siffror är tillåtet!")


