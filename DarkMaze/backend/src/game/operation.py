from src.database.operation import save_game_state
from src.game.judge import hit_obstacle, game_over, arrive_at_destination


def move_location(game_state: dict, direction: str) -> dict:
    """
    Updates the player's position in the game based on the given direction.
    Adjusts health if an obstacle is encountered and checks for game completion.
    """

    if game_over(game_state["health"]):
        return game_state

    x, y = game_state["current_position"]
    width, height = game_state["map_size"]

    # Define movement directions
    DIRECTIONS = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }

    if direction not in DIRECTIONS:
        return game_state  # Invalid direction, no movement

    dx, dy = DIRECTIONS[direction]
    new_position = [x + dx, y + dy]

    if not is_within_bounds(new_position, width, height):
        return game_state  # Out of bounds, no movement

    if hit_obstacle(tuple(new_position), game_state["current_level_name"]):
        game_state["health"] -= 1  # Reduce health on obstacle hit
    else:
        update_player_position(game_state, new_position)

    if arrive_at_destination(game_state["current_level_name"], game_state["current_position"]):
        game_state["health"] = 666  # Mark game as won

    save_game_state_to_db(game_state)  # Save the game state
    return game_state

# Helper function to check if the new position is within bounds
def is_within_bounds(position, width, height) -> bool:
    x, y = position
    return 0 <= x < width and 0 <= y < height

# Helper function to update the player's position
def update_player_position(game_state: dict, new_position: list):
    if new_position not in game_state["path"]:
        game_state["path"].append(new_position)
    game_state["current_position"] = new_position

# Helper function to save the game state
def save_game_state_to_db(game_state: dict):
    save_game_state(
        game_state["username"],
        game_state["current_level_name"],
        game_state["map_size"],
        game_state["health"],
        game_state["path"],
        game_state["current_position"],
    )
