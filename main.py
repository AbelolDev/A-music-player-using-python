import pygame
import os

# Lista global para almacenar la lista de reproducción
playlist = []

def clear_screen():
    """Clears the screen based on the operating system."""
    if os.name == 'posix':  # Linux y macOS
        _ = os.system('clear')
    elif os.name == 'nt':  # Windows
        _ = os.system('cls')
    else:
        print("Unable to detect a compatible operating system for screen clearing.")

def choose_music():
    """Allows the user to choose another music file and adds it to the playlist."""
    validation_exit = False
    while validation_exit == False:
        new_music_file = input("Enter the path to the new music file: ")
        if os.path.exists(new_music_file):
            playlist.append(new_music_file)
            print(f"Added '{new_music_file}' to playlist.")
        else:
            print(f"File '{new_music_file}' not found.")
        
        print("Would you like to add another music file?")
        print("1-) Yes")
        print("2-) No")
        try:
            option = int(input(">>> "))
            if option == 2:
                break
        except ValueError:
            print("Invalid option")
        input("Press ENTER to continue")

def init_music_player(music_file):
    """Initializes pygame mixer and loads the music file."""
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)

def play_music():
    """Plays the music in the playlist sequentially."""
    if not playlist:
        print("The playlist is empty.")
        input("Press ENTER to continue")
        return
    else:
        for music_file in playlist:
            if os.path.exists(music_file):
                init_music_player(music_file)
                pygame.mixer.music.play()
                print(f"Playing {music_file}")
            else:
                print(f"File '{music_file}' not found.")
    input("Press ENTER to continue")

def pause_music():
    """Pauses or unpauses the music depending on its current state."""
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        print("Music paused")
    else:
        pygame.mixer.music.unpause()
        print("Music unpaused")
    input("Press ENTER to continue")

def stop_music():
    """Stops the music."""
    pygame.mixer.music.stop()
    print("Music stopped")
    input("Press ENTER to continue")

def add_to_playlist():
    """Allows the user to add music files to the playlist."""

    validation_exit = False

    while validation_exit == False:
        new_music_file = input("Enter the path to the new music file: ")
        if os.path.exists(new_music_file):
            playlist.append(new_music_file)
            print(f"Added '{new_music_file}' to playlist.")
        else:
            print(f"File '{new_music_file}' not found.")
        
        print("Would you like to add another music file?")
        print("1-) Yes")
        print("2-) No")
        try:
            option = int(input(">>> "))
            if option == 2:
                break
        except ValueError:
            print("Invalid option")
        input("Press ENTER to continue")

def main():
    """Main function to run the music player."""
    validation = False

    while validation == False:
        clear_screen()
        # Get user input for the command
        print("Select an option: ")
        print("1-) Play the loaded music")
        print("2-) Pause/unpause music")
        print("3-) Stop the music")
        print("4-) Choose another music file")
        print("5-) Add music to playlist")
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
                    add_to_playlist()
                case 6:
                    print("Goodbye!")
                    pygame.mixer.quit()
                    validation = True
                case _:
                    print("Invalid option")
                    input("Press ENTER to continue")
        except ValueError:
            print("Invalid option")
            input("Press ENTER to continue")

if __name__ == "__main__":
    main()
