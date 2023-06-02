"""
2D Quadcopter AI by Alexandre Sajus

More information at:
https://github.com/AlexandreSajus/Quadcopter-AI

This is the main game where you can compete with AI agents
Collect as many balloons within the time limit
"""

import sys
from balloon import balloon
from snowglobe import snowglobe


def main(game: str = "balloon") -> None:
    """
    Runs the selected game.

    Args:
        game (str): The game to run (balloon, snowglobe)
    """
    if game == "balloon":
        balloon()
    elif game == "snowglobe":
        snowglobe()
    else:
        print(f"Unknown tracking library: {game} (expected: balloon or snowglobe)")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
