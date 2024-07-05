import pygame
import os

def clear_screen():
    """Clears the screen based on the operating system."""
    if os.name == 'posix':  # Linux and macOS
        _ = os.system('clear')
    elif os.name == 'nt':  # Windows
        _ = os.system('cls')
    else:
        print("Unable to detect a compatible operating system for screen clearing.")


def init_music_player(music_file):
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the music file
    pygame.mixer.music.load(music_file)

def play_music():
    # Play the loaded music
    pygame.mixer.music.play()
    print("Playing music")

def pause_music():
    # Pause or unpause the music depending on its current state
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        print("Music paused")
    else:
        pygame.mixer.music.unpause()
        print("Music unpaused")

def stop_music():
    # Stop the music
    pygame.mixer.music.stop()
    print("Music stopped")

def main():

    global validation
    validation = False

    # Path to the music file
    music_file = "env/programa/music/music_test.mp31"
    # Initialize the music player
    init_music_player(music_file)

    while validation == False:
        #clear_screen()
        # Get user input for the command
        print("Select a option: ")
        print("1-) Play the loaded music")
        print("2-) Pause/unpause music")
        print("3-) Stop the music")
        print("4-) Exit")

        try:
            option = int(input(">>> "))
            match option:
                case 1:
                    play_music()
                case 2:
                    pause_music()
                case 3:
                    stop_music()
                case 4:
                    print("Good bye¡")
                    validation = True
                case _:
                    print("Invalid option")
        except ValueError:
            print("Invalid option")
            continue

if __name__ == "__main__":
    main()
