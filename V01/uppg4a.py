# 4 - Fler övningar
print("1a - program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg.")
print("--------------------------------------------------------------------------------------")
s: int = 470000
t: float = 0

x = input("Ange vilken medelhastighet (km/tim), du uppskattar hölls mellan Stockholm - Göteborg (t.ex. 110, 90): ")
if x.isnumeric():
    v = float(x)
    t = (470000 * 3.6) / v
    print(f"Det tog: {t}, att köra {s} meter mellan Stockholm och Göteborg")
else:
    print("Endast siffror är tillåtet att mata in")





