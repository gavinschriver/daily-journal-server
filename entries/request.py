import sqlite3
import json
from models import Entry

def get_all_entries():
    with sqlite3.connect("./dailyjournal.db") as con:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.topics,
            e.entry,
            e.moodId,
            e.instructorId
        FROM Entries e
        """)
        entries = []
        data = cursor.fetchall()
        for row in data:
            entries.append(Entry(row['id'], row['date'], row['topics'], row['entry'], row['moodId'], row['instructorId']).__dict__)
    return json.dumps(entries)