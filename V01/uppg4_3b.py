# 4 - Fler övningar
# 3b

# Importerar klasserna datetime och timedelta från modulen datetime
from datetime import datetime, timedelta

# timedelta is a data type within the datetime module used to represent durations or differences between two points in time.

print("program som talar om vilket datum det är om 7 dagar.")
print("----------------------------------------------------")

# Dagens datum
date_today = datetime.today()
date_in_seven_days = date_today + timedelta(days=7)

# Formatterad utskrift använder funktionen strftime för att formatera datum enligt: 2025-01-25
print(f"Datum om sju dagar: {date_in_seven_days.strftime('%Y-%m-%d')}")









