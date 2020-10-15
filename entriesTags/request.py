import sqlite3
import json
from models import EntryTag

def get_all_entriesTags():
    with sqlite3.connect("./dailyjournal.db") as con:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute("""
        SELECT
            et.id,
            et.tagId,
            et.entryId
        FROM EntriesTags et
        """)
        entriesTags = []
        data = cursor.fetchall()
        for row in data:
            entriesTags.append(EntryTag(row['id'], row['tagId'], row['entryId']).__dict__)
    return json.dumps(entriesTags)