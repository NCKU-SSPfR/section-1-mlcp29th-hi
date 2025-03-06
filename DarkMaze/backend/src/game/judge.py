import json
import os
import re
import numpy as np

def parse_map(map_string: str, map_size: tuple[int, int], reversal_nodes=None) -> np.ndarray:
    """Parses a given map string into a binary matrix representation."""
    if reversal_nodes is None:
        reversal_nodes = []

    width, height = map_size
    filtered_chars = re.sub(r'[^a-zA-Z]', '', map_string)
    binary_values = [bin(ord(c))[2:].zfill(8) for c in filtered_chars]

    parsed_map = []
    for binary in binary_values:
        parsed_map.extend([int(binary[:4], 2) % 2, int(binary[4:], 2) % 2])

    # Ensure the map fits within the defined dimensions
    parsed_map.extend([0] * (width * height - len(parsed_map)))
    maze_array = np.array(parsed_map[:width * height]).reshape((height, width))

    # Apply reversals
    for x, y in reversal_nodes:
        if 0 <= x < height and 0 <= y < width:
            maze_array[y, x] = 1 - maze_array[y, x]

    return maze_array

def load_maze_from_json(maze_level_name: str) -> dict:
    """Loads a maze configuration from a JSON file."""
    file_path = os.path.join("src", "game", "maze_level", f"{maze_level_name}.json")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return {
        "maze_level_name": data.get("maze_level_name", "Unknown Level"),
        "map_size": tuple(data.get("map_size", [10, 10])),
        "starting_position": tuple(data.get("starting_position", [0, 0])),
        "end_position": tuple(data.get("end_position", [0, 0])),
        "map": parse_map(data.get("map", ""), tuple(data.get("map_size", [10, 10])), data.get("reversal_node", [])),
    }

def hit_obstacle(position: tuple[int, int], maze_level_name: str) -> bool:
    """Checks if a given position in the maze is an obstacle (1) or free space (0)."""
    x, y = position
    maze_data = load_maze_from_json(maze_level_name)
    grid = maze_data["map"]

    return not (0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]) or grid[y, x] == 1

def game_over(health: int) -> bool:
    """Checks if the game is over based on the player's health."""
    return health in {0, 666}

def arrive_at_destination(maze_level_name: str, current_position: tuple[int, int]) -> bool:
    """Checks if the player has arrived at the maze's destination."""
    file_path = os.path.join("src", "game", "maze_level", f"{maze_level_name}.json")

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return tuple(current_position) == tuple(data.get("end_position", [0, 0]))
