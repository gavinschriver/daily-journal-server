import sqlite3
import json
from models import Instructor

def get_all_instructors():
    with sqlite3.connect("./dailyjournal.db") as con:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute("""
        SELECT 
            i.id,
            i.first_name,
            i.last_name,
            i.expertise
        FROM Instructors i    
        """)
        instructors = []
        dataset = cursor.fetchall()
        for row in dataset:
            instructors.append(Instructor(row['id'], row['first_name'], row['last_name'], row['expertise']).__dict__)
        return json.dumps(instructors)    