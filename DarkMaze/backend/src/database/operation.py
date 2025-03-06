import sqlite3
import json

# Database connection
conn = sqlite3.connect("game.db")
cursor = conn.cursor()

def create_user(username):
    """Create a new user and initialize their game state."""
    try:
        cursor.execute(
            """
            INSERT INTO game_state 
            (username, current_level_name, map_size, health, path, current_position)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (username, "maze-level-1", json.dumps([10, 10]), 3, json.dumps([[1, 0]]), json.dumps([1, 0]))
        )
        conn.commit()
        print(f"User {username} has been created and game state initialized!")
    except sqlite3.IntegrityError:
        print(f"User {username} already exists, no need to create!")


def reset_game_state(username):
    """Reset the game state for an existing user."""
    cursor.execute("SELECT id FROM game_state WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        cursor.execute(
            """
            UPDATE game_state 
            SET current_level_name = ?, map_size = ?, health = ?, path = ?, current_position = ?
            WHERE username = ?
            """,
            ("maze-level-1", json.dumps([10, 10]), 3, json.dumps([[1, 0]]), json.dumps([1, 0]), username)
        )
        conn.commit()
        print(f"Game state reset! (User: {username})")
    else:
        print(f"User {username} does not exist, please create an account first!")


def save_game_state(username, current_level_name, map_size, health, path, current_position):
    """Save or update the game state for an existing user."""
    cursor.execute("SELECT id FROM game_state WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        cursor.execute(
            """
            UPDATE game_state 
            SET current_level_name = ?, map_size = ?, health = ?, path = ?, current_position = ?
            WHERE username = ?
            """,
            (current_level_name, json.dumps(map_size), health, json.dumps(path), json.dumps(current_position), username)
        )
        conn.commit()
        print(f"Game state updated! (User: {username})")
    else:
        print(f"User {username} does not exist, please create an account first!")


def get_latest_game_state(username):
    """Retrieve the latest game state for the given username."""
    cursor.execute("SELECT * FROM game_state WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if result:
        game_state = {
            "username": result[1],
            "current_level_name": result[2],
            "map_size": json.loads(result[3]),
            "health": result[4],
            "path": json.loads(result[5]),
            "current_position": json.loads(result[6]),
            "message": "Load successful",
            "cookies": [],
            "status": 1
        }
        return game_state
    
    print(f"Cannot find game state for user {username}!")
    return None
