'''
Perioden är 1.1.2026–31.12.2035 = 10 år × 12 månader = 120 element
eg. måste skapa en lista med 120 separata MonthList-instanser
'''

from linked_list import MonthList

months = [MonthList() for _ in range(120)]

# function som räknar ut vilket index (0–119) en viss månad/år ska ha i months listan
def month_index(year, month):
    return (year - 2026) * 12 + (month - 1)
