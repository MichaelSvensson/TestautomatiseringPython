# Uppgift 4 - Temperaturomvandling
# Skriv ett program som kan omvandla en temperatur i grader från Celsius till Fahrenheit eller tvärtom.
# Version 2
# Fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit.
# Sedan räknar programmet om till den andra temperaturen.

antal_grader_celsius = 0.0
antal_grader_fahrenheit = 0.0



try:
    antal_grader_celsius = float(input("Skriv in en temperatur i grader Celsius: "))
    antal_grader_fahrenheit = 1.8 * antal_grader_celsius + 32
    print(f"Det blir {antal_grader_fahrenheit} grader i Fahrenheit")
except ValueError:
    print("Antalet grader i Celsius ska anges enligt följande: [12] [15.6], alltså heltal eller decimaltal")



