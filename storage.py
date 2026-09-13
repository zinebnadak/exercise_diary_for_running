'''
Lagringen:
- En fil per månad, data/2026-08.json
- Filen skrivs om varje gång ett pass läggs till/tas bort/redigeras för den månaden
- Behöver kunna konvertera Session/Duration/date till/från JSON-vänligt format (datum som ISO-sträng)
'''

import json
import os
from datetime import date
from models import Session, Duration

# konvertera Session till JSON , eg dictrionary
def session_to_dict(session):
    return {
        "description": session.description,
        "date": session.date.isoformat(),  # date -> ISO-sträng
        "distance": session.distance,
        "duration": {
            "hours": session.duration.hours,
            "minutes": session.duration.minutes,
            "seconds": session.duration.seconds,
        }
    }

# konvertera JSON till Session
def dict_to_session(d):
    return Session(
        description=d["description"],
        date=date.fromisoformat(d["date"]),  # ISO-sträng -> date
        distance=d["distance"],
        duration=Duration(**d["duration"]) #pointer
    )

# sparar data till JSON fil
def save_month(year, month, month_list):
    os.makedirs("data", exist_ok=True) # skapa permanent mapp
    filename = f"data/{year}-{month:02d}.json" #skapar filnamnet
    sessions_data = [session_to_dict(s) for s in month_list]
    with open(filename, "w") as f: #skapar och populerar data i filen med filnamnet
        json.dump(sessions_data, f, indent=2)

# läser filen om den finns
def load_month(year, month, month_list):
    filename = f"data/{year}-{month:02d}.json"
    if not os.path.exists(filename):
        return
    with open(filename, "r") as f:
        sessions_data = json.load(f)
    for d in sessions_data:
        month_list.insert(dict_to_session(d))