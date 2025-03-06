import sqlite3

def initialize():
    """Initialize the database and create the game_state table if it does not exist."""
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS game_state (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            current_level_name TEXT NOT NULL,
            map_size TEXT NOT NULL,
            health INTEGER NOT NULL,
            path TEXT NOT NULL,
            current_position TEXT NOT NULL
        )
        """
    )
    
    conn.commit()
    conn.close()
