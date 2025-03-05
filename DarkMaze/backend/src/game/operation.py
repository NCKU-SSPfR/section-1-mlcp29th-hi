from ..database.operation import save_game_state
from .judge import hit_obstacle, game_over, arrive_at_destination


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

    # Compute new position
    if direction in DIRECTIONS:
        dx, dy = DIRECTIONS[direction]
        new_x, new_y = x + dx, y + dy

        # Ensure movement stays within bounds
        if 0 <= new_x < width and 0 <= new_y < height:
            new_position = [new_x, new_y]

            if hit_obstacle(new_position, game_state["current_level_name"]):
                game_state["health"] -= 1  # Reduce health on obstacle hit
            else:
                if new_position not in game_state["path"]:
                    game_state["path"].append(new_position)

                game_state["current_position"] = new_position

            # Check if the player has reached the destination
            if arrive_at_destination(game_state["current_level_name"], game_state["current_position"]):
                game_state["health"] = 666  # Mark game as won

    # Update game state in the database
    save_game_state(
        game_state["username"],
        game_state["current_level_name"],
        game_state["map_size"],
        game_state["health"],
        game_state["path"],
        game_state["current_position"],
    )

    return game_state
