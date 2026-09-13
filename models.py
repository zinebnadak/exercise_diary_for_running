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

