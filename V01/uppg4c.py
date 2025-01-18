
# 4 - Fler övningar
# 1c

print("1c - program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg.")
print("programmet ska svara i hela timmar och minuter.")
print("--------------------------------------------------------------------------------------")
s: int = 470000
t: float = 0

x = input("Ange vilken medelhastighet (km/tim), du uppskattar hölls mellan Stockholm - Göteborg (t.ex. 110, 90): ")
if x.isnumeric():
    v = float(x)
    t = (470000 * 3.6) / v  # t angivet i sekunder

    # Omvandla till minuter istället för sekunder
    t = t/60                # t angivet i minuter

    # Omvandla antalet minuter till antal timmar och minuter
    antal_tim = t//60

    antal_min = t%60

    print(f"Det tar: {antal_tim} timmar och {antal_min} minuter att köra mellan Stockholm och Göteborg om man kör med en medelhastighet av {v} km/tim")

else:
    print("Endast siffror är tillåtet att mata in")





