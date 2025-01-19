# Uppgift 1
# 1.	Vad är syftet med koden?
      # Att ge mer rabatt beroende på om man köper för mer än 100 kr (10%) eller mer än eller exakt 200 kr (25%)

# 2.	Testkör koden med några olika värden.

# 3.	Finns det några direkta fel i koden? (fel som gör att programmet kraschar)
      # a. final_price måste göras om till en sträng eftersom i koden försöker man slå ihop två strängar
      # b. Om man anger ett icke numerisk värde, tex. ett tecken, kraschar programmet.

# 4.	Finns det logiska fel? (programmet gör något annat än det är tänkt)
      # c. Om man anger >= 200, får man 10%+25% = 35% i rabatt vilket är fel. Borde vara endast 25% rabatt (level 2)

# 5.	Diskutera möjliga lösningar på felen ni hittat.
      # a. str(final_price) istället för endast final_price
      # b. x = input("Välkommen, köp något dyrt: ")
      #    if x.isnumeric():
      #       price = float(x)
# else:
#     print("Endast siffror är giltigt att mata in!")
      # c. if (price > level1) and (price < level2): istället för endast if price > level1

# 6.	Diskutera möjliga förbättringar på koden.
      # Ta bort variabeln is_member= False etersom den inte används senare i programmet.
      # Ange att priset ska anges i rätt valuta.
      # Skriva ut priset i rätt valuta.
      # Verifiera att man endast kan skriva in siffor och att andra tecken inte ä tillåtna



is_member = False
level1 = 100
level2 = 200
discount = 0

price = 0.0

# price = input("Välkommen, köp något dyrt: ")
# price = float(price)

x = input("Välkommen, köp något dyrt: ")
if x.isnumeric():
    price = float(x)
else:
    print("Endast siffror är giltigt att mata in!")

if (price > level1) and (price < level2):
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
if price >=  level2:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price * (100 - discount) / 100
print("Efter rabatter blir priset..." + str(final_price))
