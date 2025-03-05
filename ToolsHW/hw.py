import webbrowser
import sys
import os

youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def open_video():
    """Opens the YouTube video."""
    webbrowser.open(youtube_url)
    os.system("echo 'Rickroll incoming...'")

def get_user_input():
    """Prompts the user for the correct answer and plays video if correct."""
    while True:
        user_input = input("1 times 1 = ? ")
        if user_input == "1":
            open_video()
            break
        elif user_input.lower() == "exit":
            sys.exit()
        else:
            print("Wrong! Try again.")

if __name__ == "__main__":
    get_user_input()
