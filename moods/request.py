import sqlite3
import json
from models import Mood

def get_all_moods():
    with sqlite3.connect("./dailyjournal.db") as con:
        con.row_factory = sqlite3.Row
        c = con.cursor()
        c.execute("""
        SELECT
            m.id,
            m.label
        FROM Moods m    
        """)
        moods = []
        dataset = c.fetchall()
        for row in dataset:
            moods.append(Mood(row['id'], row['label']).__dict__)
        return json.dumps(moods)