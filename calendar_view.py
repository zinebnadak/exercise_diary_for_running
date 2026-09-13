'''
Kalendervy:
- skriv ut en månad i kalenderformat
- markera dagar med pass
'''

import calendar

WEEKDAYS = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

# funktion som skriver ut kalendervyn som användargränssnitt till terminalen 
def print_calendar(year, month, months, month_index):
    idx = month_index(year, month)
    days_with_sessions = {s.date.day for s in months[idx]}  # ett set med dagar som har pass

    first_weekday, num_days = calendar.monthrange(year, month) # monthrange ger vilken veckodag månaden börjar på och hur många dagar månaden har

    print(f"\n{calendar.month_name[month]} {year}")
    print(" ".join(WEEKDAYS))

    line = "   " * first_weekday  # tomrum innan första dagen
    for day in range(1, num_days + 1):
        marker = "*" if day in days_with_sessions else " "
        line += f"{day:2d}{marker}"
        if (day + first_weekday) % 7 == 0:
            print(line)
            line = ""
    if line:
        print(line)