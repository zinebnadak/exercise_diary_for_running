from dataclasses import dataclass
from datetime import date

@dataclass 
class Duration:
    hours: int
    minutes: int 
    seconds: int 
    

@dataclass 
class Session:
    description: str 
    date: date 
    distance: float 
    duration: Duration 

'''
Test with:

python3 -c "from models import Session, Duration; from datetime import date; s = Session('Morgonpass', date(2026, 1, 15), 5.2, Duration(0, 28, 30)); print(s)"
'''