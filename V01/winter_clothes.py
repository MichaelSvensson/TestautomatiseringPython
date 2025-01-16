# 2a
print("Uppgift 2a")
print("----------")
pris: int = 2000
rea_procent = 50
slut_pris: float = pris * rea_procent / 100
print(f"Jackan kostar: {pris} kr")
print(f"Jackan är på rea, {rea_procent} %")
print(f"Att betala: {slut_pris}")
print("------------------")

# 2b
print("Uppgift 2b")
pris: int = 2000
procent_sats = input("Ange procent-sats (tex: 10.45): ")
procent = float(procent_sats)
rabatt_i_kr = float(pris*(procent/100))
print(f"Rabatt i kr: {rabatt_i_kr}")
slut_pris: float = pris - rabatt_i_kr
print(f"procent: {procent}%, som är: {rabatt_i_kr} kr")
print(f"Då ska jackan kosta {pris} - {rabatt_i_kr} == {slut_pris}")
