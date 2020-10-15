import sqlite3
import json
from models import Tag

def get_all_tags():
    with sqlite3.connect("./dailyjournal.db") as con:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute("""
        SELECT
            t.id,
            t.subject
        FROM Tags t
        """)
        tags = []
        data = cursor.fetchall()
        for row in data:
            tags.append(Tag(row['id'], row['subject']).__dict__)
    return json.dumps(tags)