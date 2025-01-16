# x = 100  biljettpris
# y = 200   pengar på fickan
# print("Det blir " + (y - x) " kronor över.")
# z = 200 - 100 / 2
# print("Hälften är: " + z)

# Correct code snippets

# x = 100   biljettpris
# y = 200   pengar på fickan
# print("Det blir " + "(y - x)" + "kronor över.")
# z = (200 - 100) / 2
# print("Hälften är: ", z)

# Better namnes on variables
# ticket_price = 100  # biljettpris
# pocket_money = 200  # pengar på fickan
# print("Det blir ", (pocket_money-ticket_price), "kronor över.")
# half = (200 - 100) / 2
# print("Hälften är: ", half)

# Formating the print command
ticket_price = 100  # biljettpris
pocket_money = 200  # pengar på fickan
print(f"Det blir, {pocket_money-ticket_price}, kronor över.")
half = (200 - 100) / 2
print(f"Hälften är: , {half}")