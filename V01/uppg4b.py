# 4 - Fler övningar
# 4b.

print("1a - program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg.")
print("--------------------------------------------------------------------------------------")
s: int = 470000
t: float = 0

x = input("Ange vilken medelhastighet (km/tim), du uppskattar hölls mellan Stockholm - Göteborg (t.ex. 110, 90): ")
if x.isnumeric():
    v = float(x)
    t = (470000 * 3.6) / v  # t angivet i sekunder

    # Omvandla till minuter istället för sekunder
    t = t/60                # t angivet i minuter

    print(f"Det tog: {t} minuter, att köra {s/1000} km mellan Stockholm och Göteborg")

else:
    print("Endast siffror är tillåtet att mata in")





