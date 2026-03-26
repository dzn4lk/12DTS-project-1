import random
player_health = 100
has_potion = True

inventory = []
pieces_collected = 0
TOTAL_PIECES = 4


def clear_screen():
    print("\n" * 50)

def give_piece():
    global pieces_collected

    print("\nYou obtained a Trial Piece!\n")
    inventory.append("Trial Piece")
    pieces_collected += 1

def title_art():
    print(r"""
___________.__                __   .__                           __         .__.__   
\__    ___/|  |__   ____     |  | _|__| ____    ____  ______   _/  |________|__|  |  
  |    |   |  |  \_/ __ \    |  |/ /  |/    \  / ___\/  ___/   \   __\_  __ \  |  |  
  |    |   |   Y  \  ___/    |    <|  |   |  \/ /_/  >___ \     |  |  |  | \/  |  |__
  |____|   |___|  /\___  >   |__|_ \__|___|  /\___  /____  >    |__|  |__|  |__|____/
                \/     \/         \/       \//_____/     \/                          
    """)


def show_inventory():
    print("\n=== INVENTORY ===")
    if len(inventory) == 0:
        print("Empty")
    else:
        for item in inventory:
            print("-", item)
    input("\nPress ENTER...")

def puzzle_room():
    print("\n=== PUZZLE ROOM ===\n")

    answer = input("What has to be broken before you can use it? ").lower(
    if answer == "egg":
        print("\nCorrect!")
        give_piece()
    else:
        print("\nWrong answer.")

    input("Press ENTER...")
def treasure_room():
    print("treasure_room")

def dungeon_room():
    print("dungeon_room")


def start_menu():
    while True:
        clear_screen()
        title_art()

        print("\n1. Start Game")
        print("2. Instructions")
        print("3. Quit")

        choice = input("\nChoose: ")

        if choice == "1":
            intro_story()
        elif choice == "2":
            instructions()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


def instructions():
    clear_screen()
    title_art()

    print("\nCollect all 4 Trial Pieces to win.")
    print("Fight enemies, solve puzzles, and explore rooms.\n")

    input("Press ENTER...")


def intro_story():
    clear_screen()
    title_art()

    print("\nThe torches flicker as you step into the King’s throne room...")
    print("The air is heavy. Silent. Watching.\n")

    print('"Many have stood where you stand now," the King says.')
    print('"All believed they were worthy."\n')

    print("He rises slowly from his throne.\n")

    print('"Beneath this castle lies the Trial Chambers."')
    print('"Strength alone will not save you."')
    print('"Mind, courage, and will... these decide your fate."\n')

    print("A hidden door behind the throne creaks open.")
    print("Darkness waits below.\n")

    print('"Enter... and prove yourself."')

    input("\nPress ENTER to descend into the trials...")
    room_selection()



def room_selection():
    while True:
        clear_screen()
        title_art()

        print("\n=== CHOOSE YOUR PATH ===\n")
        print(f"Pieces: {pieces_collected}/{TOTAL_PIECES}\n")

        print("1. First Trial")
        print("2. Whispering Room")
        print("3. Forgotten Dungeon")
        print("4. Hidden Vault")
        print("5. Inventory")
        print("6. Quit to Menu")

        choice = input("\nChoose: ")

        if choice == "1":
            training_room()
        elif choice == "2":
            puzzle_room()
        elif choice == "3":
            dungeon_room()
        elif choice == "4":
            treasure_room()
        elif choice == "5":
            show_inventory()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
            input("Press ENTER...")



def training_room():
    clear_screen()
    title_art()

    print("\n=== THE FIRST TRIAL ===\n")

    print("You step into a circular stone chamber.")
    print("The door slams shut behind you.\n")

    print("A lone guard stands in the center.")
    print("His armor is worn.\n")

    print('"Another challenger...".')
    print('"I was once like you."')
    print('"Now I am part of the trial."\n')

    print("He slowly raises his sword.\n")

    print('"If you wish to pass... you must defeat me."')

    input("\nPress ENTER to fight...")

    print("\nThe guard drops to one knee.")
    print('"Good... you may yet survive this place..."\n')





    give_piece()
    input("Press ENTER...")


start_menu()