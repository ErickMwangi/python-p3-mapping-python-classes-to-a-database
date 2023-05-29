from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            album TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()

        row = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()
        if row is not None:
            self.id = row[0]

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song
