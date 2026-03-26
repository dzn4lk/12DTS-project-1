player_health = 100
has_potion = True

inventory = []
pieces_collected = 0
TOTAL_PIECES = 3

def show_inventory():
    print("\n=== INVENTORY ===")
    if len(inventory) == 0:
        print("Empty")
    else:
        for item in inventory:
            print("-", item)
    input("\nPress any key to continue...")


print("\n" * 50)
print(r"""
___________.__                __   .__                           __         .__.__   
\__    ___/|  |__   ____     |  | _|__| ____    ____  ______   _/  |________|__|  |  
  |    |   |  |  \_/ __ \    |  |/ /  |/    \  / ___\/  ___/   \   __\_  __ \  |  |  
  |    |   |   Y  \  ___/    |    <|  |   |  \/ /_/  >___ \     |  |  |  | \/  |  |__
  |____|   |___|  /\___  >   |__|_ \__|___|  /\___  /____  >    |__|  |__|  |__|____/
                \/     \/         \/       \//_____/     \/                          
    """)



print("\nThe kingdom stands on the edge of ruin...")
print("Enemies gather beyond the borders, and fear spreads.\n")

print("The King has called for a champion.")
print("Not by birth... but by strength and mind.\n")

print("Beneath the castle lie the Trial Chambers.")
print("Many have entered...")
print("None have returned.\n")

print("Tonight... YOU step forward.\n")

print("Survive the trials.")
print("Prove your worth.")
print("Become the champion.\n")

input("Press any key to begin your trial...")




def room_selection():
    while True:
        print("\n=== CHOOSE A ROOM ===\n")
        print("1. Training Chamber (Combat)")
        print("2. Puzzle Room (Riddle)")
        print("3. Dungeon Room (Hard Combat)")
        print("4. Treasure Room (Reward)\n")

        print("5. Check Inventory")
        print("6. Quit to Menu")

        choice = input("\nChoose an option: ")

        if choice == "1":
            training_room()
        elif choice == "2":
            puzzle_room()
        elif choice == "3":
            combat_room()
        elif choice == "4":
            treasure_room()
        elif choice == "5":
            show_inventory()
        elif choice == "6":
            start_menu()
            break
        else:
            print("Invalid choice")
            print("Press enter")
