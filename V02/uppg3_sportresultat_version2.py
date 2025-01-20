# Uppg3 - Sportresultat
# Tottenham spelar mot Liverpool i Champions League.
# Skriv ett program som frågar användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.
#
# Version 2

amount_goal_tottenham = 0
amount_goal_liverpool = 0
oavgjort = False

try:
    amount_goal_tottenham = int(input("Hur många mål gjorde Tottenham? "))
    amount_goal_liverpool = int(input("Hur många mål gjorde Liverpool? "))
    if amount_goal_tottenham <0 or amount_goal_tottenham <0:                # Avbryter programmet om något av lagen har angivit negativt antal mål
        print("Antal mål kan inte anges som negativa <0! ")
        exit()

    if amount_goal_tottenham > amount_goal_liverpool:
        print("Tottenham vann!")
    elif amount_goal_liverpool > amount_goal_tottenham:
        print("Liverpool vann!")
    else:
        oavgjort = amount_goal_tottenham == amount_goal_tottenham
    if oavgjort:
        print("Det blev oavgjort!")

except ValueError:
    print("Antal mål ska anges i hela mål och i siffror")
