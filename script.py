import random
import pyfiglet
# Global variables
player_health = 100
has_potion = False
pieces_collected = 0
TOTAL_PIECES = 4


rooms_done = [False, False, False, False]  # training, puzzle, dungeon, treasure


def clear_screen():
    print("\n" * 50)
def title_art():
    custom_art = pyfiglet.figlet_format("The   kings   trials", font="Epic")
    print(custom_art)


def give_piece():
    global pieces_collected
    pieces_collected += 1
    print("\nYou collected a Trial Piece! (" + str(pieces_collected) + "/" + str(TOTAL_PIECES) + ")\n")


def show_status():
    print("Health:", player_health, "| Potion:", "Yes" if has_potion else "No", "| Pieces:", str(pieces_collected) + "/" + str(TOTAL_PIECES))


def instructions():
    clear_screen()
    title_art()
    print()
    print("Your goal is to collect all 4 Trial Pieces.")
    print()
    print("  Room 1 - The First Trial: defeat the guard")
    print("  Room 2 - The Puzzle Room: answer riddles")
    print("  Room 3 - The Dungeon: fight a creature")
    print("  Room 4 - The Vault: pick the right chest")
    print()
    print("You start with 100 health and no potions (One of the rooms has a potion. It is up to you to find it or not).")
    input("Press ENTER to go back...")


def intro_story():
    clear_screen()
    title_art()
    print()
    print("You stand before the King in his throne room.")
    print("The air is cold and still.")
    print()
    print("The King speaks:")
    print('"Below this castle are the Trial Chambers."')
    print('"Only the worthy may pass all four."')
    print()
    print("A hidden door creaks open behind the throne.")
    print("Darkness waits below.")
    print()
    input("Press ENTER to begin the trials...")


def training_room():
    global rooms_done, has_potion
    clear_screen()
    title_art()
    print()
    print("=== THE FIRST TRIAL ===")
    print()
    if rooms_done[0]:
        print("You have already completed this trial.")
        input("Press ENTER...")
        return
    print("A guard stands in the centre of the room.")
    print('"You must defeat me to pass," he says.')
    print()
    input("Press ENTER to fight...")
    print()
    print("You charge forward. After a fierce fight, the guard falls.")
    print('"Well done. Move on," he says from the floor.')
    print('He slides you a potion of healing.')
    print()
    give_piece()
    rooms_done[0] = True
    has_potion = True
    input("Press ENTER...")



def puzzle_room():
    global rooms_done
    clear_screen()
    title_art()
    print()
    print("=== THE PUZZLE ROOM ===")
    print()
    if rooms_done[1]:
        print("You have already completed this trial.")
        input("Press ENTER...")
        return
    print("The door shuts behind you.")
    print("The room is silent except for a low hum in the walls.")
    print()
    print("Words appear carved into the stone floor:")
    print('"Five riddles await you. Answer at least 4 correctly to earn the Trial Piece."')
    print()
    input("Press ENTER to begin...")
    print()
    correct = 0
    # Riddle 1
    print("Riddle 1: What has to be cracked before you can eat it raw?")
    answer_1 = input("Your answer: ").strip().lower()
    print()
    if answer_1 == "egg":
        print("Correct! The stone glows faintly.")
        correct += 1
    else:
        print("Wrong. The answer was: egg")
        print("The stone stays dark.")
    print()
    input("Press ENTER for the next riddle...")
    print()
    # Riddle 2
    print("Riddle 2: I have hands but cannot clap. What am I?")
    answer_2 = input("Your answer: ").strip().lower()
    print()
    if answer_2 == "clock":
        print("Correct! Another stone lights up.")
        correct += 1
    else:
        print("Wrong. The answer was: clock")
        print("The stone stays dark.")
    print()
    input("Press ENTER for the next riddle...")
    print()
    # Riddle 3
    print("Riddle 3: The more you take, the more you leave behind. What am I?")
    answer_3 = input("Your answer: ").strip().lower()
    print()
    if answer_3 == "footsteps":
        print("Correct! The room brightens a little.")
        correct += 1
    else:
        print("Wrong. The answer was: footsteps")
        print("The stone stays dark.")
    print()
    input("Press ENTER for the next riddle...")
    print()
    # Riddle 4
    print("Riddle 4: I speak without a mouth and hear without ears.")
    print("         I have no body, but I come alive with the wind. What am I?")
    answer_4 = input("Your answer: ").strip().lower()
    print()
    if answer_4 == "echo":
        print("Correct! You can feel the room warming.")
        correct += 1
    else:
        print("Wrong. The answer was: echo")
        print("The stone stays dark.")
    print()
    input("Press ENTER for the last riddle...")
    print()
    # Riddle 5
    print("Riddle 5: I have cities but no houses live in them.")
    print("         I have mountains but no trees grow on them.")
    print("         I have water but no fish swim in it. What am I?")
    answer_5 = input("Your answer: ").strip().lower()
    print()
    if answer_5 == "map":
        print("Correct! The final stone lights up.")
        correct += 1
    else:
        print("Wrong. The answer was: map")
        print("The final stone stays dark.")
    print()
    # Result
    print("You answered " + str(correct) + " out of 5 correctly.")
    print()
    if correct >= 4:
        print("The voice returns: \"Well done. Your mind is sharp.\"")
        print("\"Few make it this far. You have earned the Trial Piece.\"")
        give_piece()
        rooms_done[1] = True
    else:
        print("The voice returns: \"Not enough. You needed at least 4 correct.\"")
        print("\"Study harder and return when you are ready.\"")
    input("Press ENTER...")







def dungeon_room():
    global player_health, has_potion, rooms_done
    clear_screen()
    title_art()
    print()
    print("=== THE DUNGEON ===")
    print()
    if rooms_done[2]:
        print("You have already completed this trial.")
        input("Press ENTER...")
        return
    print("A creature steps out of the shadows.")
    print('"This is my dungeon," it growls.')
    print()
    creature_health = 50
    player_combat_health = player_health
    while creature_health > 0 and player_combat_health > 0:
        print("Your health:", player_combat_health, "| Creature health:", creature_health)
        print()
        print("1. Attack")
        if has_potion:
            print("2. Use potion (+30 health)")
        print()
        choice = input("Choose: ").strip()
        print()
        if choice == "1":
            player_damage = random.randint(10, 25)
            creature_damage = random.randint(5, 15)
            creature_health -= player_damage
            player_combat_health -= creature_damage
            print("You dealt", player_damage, "damage. The creature hit you for", str(creature_damage) + ".")
        elif choice == "2" and has_potion:
            player_combat_health += 30
            has_potion = False
            print("You used your potion. Health is now", str(player_combat_health) + ".")
        else:
            print("Invalid choice. You did nothing.")
        print()
    if player_combat_health <= 0:
        print("You were defeated. You wake up outside the dungeon.")
        player_health = 20
    else:
        print("The creature is defeated!")
        player_health = player_combat_health
        give_piece()
        rooms_done[2] = True
    input("Press ENTER...")

def vault_room():
    global rooms_done
    clear_screen()
    title_art()
    print()
    print("=== THE HIDDEN VAULT ===")
    print()
    if rooms_done[3]:
        print("You have already completed this trial.")
        input("Press ENTER...")
        return
    print("Three chests sit in front of you.")
    print("A sign reads: \"One chest holds the Trial Piece.\"")
    print()
    print("Clue on Chest 1: 'The piece is not in here.'")
    print("Clue on Chest 2: 'The piece is in Chest 1.'")
    print("Clue on Chest 3: 'The piece is not in Chest 2.'")
    print("Clue on Chest 4: 'Exactly one of these chests is telling the truth.'")
    print("Clue on Chest 5: 'The piece is in Chest 3.'")
    print("Clue on Chest 6: 'Chest 5 is lying.'")
    print("Clue on Chest 7: 'The piece is not in Chest 1.'")
    print("Clue on Chest 8: 'Chest 3 and Chest 7 cannot both be true.'")
    print()
    print("Only ONE clue is true. Choose wisely.")
    print()
    choice = input("Open which chest? (1, 2, or 3): ").strip()
    print()
    if choice == "3":
        print("You open Chest 3.")
        print("Inside is the Trial Piece!")
        give_piece()
        rooms_done[3] = True
    elif choice == "1" or choice == "2":
        print("You open the chest. It is empty.")
        print("(Hint: work out which single clue can be true.)")
    else:
        print("That is not a valid chest.")
    input("Press ENTER...")


def victory_screen():
    clear_screen()
    title_art()
    print()
    print("  *** YOU WIN! ***")
    print()
    print("You climb back to the throne room with all 4 Trial Pieces.")
    print()
    print("The King stands and nods slowly.")
    print('"You are worthy. The kingdom is yours to protect."')
    print()
    print("Congratulations! You completed The King's Trial.")
    print()
    input("Press ENTER to return to the menu...")

def room_menu():
    while True:
        clear_screen()
        title_art()
        print()
        show_status()
        print()
        print("Where do you go?")
        print()
        label_1 = "1. The First Trial" + (" [DONE]" if rooms_done[0] else "")
        label_2 = "2. The Puzzle Room" + (" [DONE]" if rooms_done[1] else "")
        label_3 = "3. The Dungeon" + (" [DONE]" if rooms_done[2] else "")
        label_4 = "4. The Hidden Vault" + (" [DONE]" if rooms_done[3] else "")
        print(label_1)
        print(label_2)
        print(label_3)
        print(label_4)
        print("5. Quit to menu")
        print()
        choice = input("Choose: ").strip()
        if choice == "1":
            training_room()
        elif choice == "2":
            puzzle_room()
        elif choice == "3":
            dungeon_room()
        elif choice == "4":
            vault_room()
        elif choice == "5":
            break
        else:
            print("Please enter 1, 2, 3, 4, or 5.")
            input("Press ENTER...")
        if pieces_collected == TOTAL_PIECES:
            victory_screen()
            break



def start_menu():
    while True:
        clear_screen()
        title_art()
        print()
        print("1. Play")
        print("2. Instructions")
        print("3. Quit")
        print()
        choice = input("Choose: ").strip()
        if choice == "1":
            intro_story()
            room_menu()
        elif choice == "2":
            instructions()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3.")
            input("Press ENTER...")

start_menu()

