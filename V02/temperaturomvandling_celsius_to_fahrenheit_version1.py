# Uppgift 4 - Temperaturomvandling
# Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
# Version 1, exempel på output:
# Skriv in en temperatur i grader Celsius: 22
# Det blir 71.6 grader Fahrenheit.

antal_grader_celsius = 0.0
antal_grader_fahrenheit = 0.0

try:
    antal_grader_celsius = float(input("Skriv in en temperatur i grader Celsius: "))
    antal_grader_fahrenheit = 1.8 * antal_grader_celsius + 32
    print(f"Det blir {antal_grader_fahrenheit} grader i Fahrenheit")
except ValueError:
    print("Antalet grader i Celsius ska anges enligt följande: [12] [15.6], alltså heltal eller decimaltal")



