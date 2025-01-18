# 4 - Fler övningar
# 2
import math

print("Program som räknar ut längden på hypotenusan i en rätvinklig triangel.")
print("----------------------------------------------------------------------")

x = input("Ange sida1 i en rätvinklig triangel: (t.ex. 3 eller 4.5) ")
side1 = float(x)

y = input("Ange sida2 i en rätvinklig triangel: (t.ex. 3 eller 4.5) ")
side2 = float(y)

hypotenusan = math.sqrt(side1 * side1 + side2 * side2)
print(f"Längden på hypotenusan = {hypotenusan} i den rätvinkliga triangeln med sidorna: {side1} och {side2}.")









