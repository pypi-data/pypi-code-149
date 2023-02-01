import sqlite3


class Storage:
    """Database handler for internal program data."""

    def __init__(self, base_directory):
        self._connection = sqlite3.connect(f'{base_directory}/data.db')
        self._connection.row_factory = sqlite3.Row
        self._initialize()

    def _initialize(self):
        cursor = self._connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS session (
                description TEXT,
                cookie_id TEXT,
                is_default INTEGER,
                first_used TEXT
            );
        ''')

        self._connection.commit()
    
    def insert(self, description, cookie_id, is_default = False):
        cursor = self._connection.cursor()

        cursor.execute('''
            INSERT INTO session (
                description,
                cookie_id,
                is_default,
                first_used
            ) VALUES (
                :description,
                :cookie_id,
                :is_default,
                datetime()
            );
        ''', {
            'description': description,
            'cookie_id': cookie_id,
            'is_default': int(is_default)
        })

        self._connection.commit()

        return cursor.lastrowid
    
    def update(self, session):
        cursor = self._connection.cursor()

        cursor.execute('''
            UPDATE session SET
                description = :description,
                cookie_id = :cookie_id,
                is_default = :is_default
            WHERE rowid = :id
        ''', {
            'id': session['rowid'],
            'description': session['description'],
            'cookie_id': session['cookie_id'],
            'is_default': session['is_default']
        })

        self._connection.commit()

    def reset_default(self):
        cursor = self._connection.cursor()

        cursor.execute('''
            UPDATE session SET
                is_default = 0
        ''')

        self._connection.commit()

    def delete(self, session):
        cursor = self._connection.cursor()

        cursor.execute('''
            DELETE FROM session
            WHERE rowid = :id
        ''', {
            'id': session['rowid']
        })

        self._connection.commit()
    
    def get_one_by_id(self, id):
        cursor = self._connection.cursor()

        cursor.execute('''
            SELECT rowid, * FROM session
            WHERE rowid = :id
        ''', {
            'id': id
        })

        session = cursor.fetchone()

        if not session:
            return None
    
        return session

    def get_all(self):
        cursor = self._connection.cursor()

        cursor.execute('''
            SELECT rowid, * FROM session
        ''')

        return cursor.fetchall()