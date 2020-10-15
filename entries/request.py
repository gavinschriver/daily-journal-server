from models import mood
from models import instructor
import sqlite3
import json
from models import Entry
from models import Instructor
from models import Mood

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
            i.id instructor_id,
            i.first_name,
            i.last_name,
            i.expertise,
            m.id mood_id,
            m.label
        FROM Entries e
        JOIN Instructors i ON i.id = e.instructorId
        JOIN Moods m ON m.id = e.moodId
        """)
        entries = []
        data = cursor.fetchall()
        for row in data:
            instructor = Instructor(row['instructor_id'],row['first_name'], row['last_name'], row['expertise']).__dict__
            mood = Mood(row['mood_id'], row['label']).__dict__
            entries.append(Entry(row['id'], row['date'], row['topics'], row['entry'], mood, instructor).__dict__)
    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as con:
        con.row_factory = sqlite3.Row
        c = con.cursor()
        c.execute('''
        SELECT
            e.id,
            e.date,
            e.topics,
            e.entry,
            e.moodId,
            i.id instructor_id,
            i.first_name,
            i.last_name,
            i.expertise,
            m.id mood_id,
            m.label
        FROM Entries e
        JOIN Instructors i ON i.id = e.instructorId
        JOIN Moods m ON m.id = e.moodId
        WHERE e.id = ?        
        ''', (id, ))
        row = c.fetchone()
        instructor = Instructor(row['instructor_id'],row['first_name'], row['last_name'], row['expertise']).__dict__
        mood = Mood(row['mood_id'], row['label']).__dict__
        entry = Entry(row['id'], row['date'], row['topics'], row['entry'], mood, instructor).__dict__
        return json.dumps(entry)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as con:
        con.row_factory = sqlite3.Row
        c = con.cursor()
        c.execute('''
        DELETE FROM Entries
        WHERE Entries.id = ?
        ''', (id, ))
        if c.rowcount > 0:
            return True
        else:
            return False

