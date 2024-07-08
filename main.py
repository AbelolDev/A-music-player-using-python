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

def choose_music():
    """Allows the user to choose another music file."""
    music_file = ""
    new_music_file = input("Enter the path to the new music file: ")
    if os.path.exists(new_music_file):
        music_file = new_music_file
        init_music_player(music_file)
        print(f"New music file '{music_file}' loaded.")
        input("Press ENTER to continue")
    else:
        print(f"File '{new_music_file}' not found.")
        input("Press ENTER to continue")

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

def music_playlist():
    validation_playlist = False
    while validation_playlist == False:
        playlist = []
        new_music_file = input("Enter the path to the new music file: ")
        playlist = playlist.append(new_music_file)
        print("Would you like to enter other music?")
        print("1-) Yes")
        print("2-) No")
        try:
            option = int(input(">>> ")) 
            match option:
                case 1:
                    validation_playlist = False
                case 2:
                    print("Good bye¡")
                    input("Press ENTER to continue")
                    validation_playlist = True
        except ValueError:
            print("Invalid option")
            input("Press ENTER to continue")

def main():

    global validation
    validation = False

    choose_music()

    while validation == False:
        clear_screen()
        # Get user input for the command
        print("Select a option: ")
        print("1-) Play the loaded music")
        print("2-) Pause/unpause music")
        print("3-) Stop the music")
        print("4-) Choose another music file")
        print("5-) Add music into playlist")
        print("6-) Exit")

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
                    choose_music()
                case 5:
                    music_playlist()
                case 6:
                    print("Good bye¡")
                    pygame.mixer.quit()
                    validation = True
                case _:
                    print("Invalid option")
                    input("Press ENTER to continue")
        except ValueError:
            print("Invalid option")
            input("Press ENTER to continue")
            continue

if __name__ == "__main__":
    main()