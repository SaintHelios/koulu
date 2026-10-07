import game
from time import sleep

print(
    r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⡀⠀⠀  ⠀⣠⠀⠀⠀ ⣤⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠦⠀⠀⣤⡀⠀⠀⢠⡶⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⢸⣧⠀⢀⣴⡟⠃⠀⠀⠀⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⢾⣯⣗⡂⠀⠀⣿⡁⠀⠀⢸⣿⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠙⣿⡟⠉⠀⠀⠀⠀⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣹⣷⠀⢸⣧⠀⠀⢸⣇⣀⣀⣀⠀⠸⣧⣤⣤⣤⡄⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠛⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢴⡶⡟⠛⠁⠀⠈⠛⠀⠀⠀⠉⠉⠛⠋⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠿⠇⠀⠀⠀⠀⢀⣠⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
)

def main():
    print("\n--- Silly Fishing Shenanigans ---\n")
    
    player_name = input("Enter your name: ")
    
    # loading saved data matching the player's name
    loaded_player, loaded_lake = game.load_data(player_name)
    
    # defaulting to false
    loaded = False

    # if-statement catches load_Data() returned data
    if loaded_player != None:
        choice = input(f"Previous save for player {player_name} found, would you like to load it? (y/n)\n: ")
        
        # if the player agrees, global objects are initialised with the objects returned from load_data()
        if choice == 'y':
            
            player = loaded_player
            lake = loaded_lake
            
            print(f"Welcome back, {player.name}! Resuming from day {player.day}.")
     
            # set to true, so the next if-statement doesn't trigger
            loaded = True
            sleep(2)
        else:
            print("Starting a new game...\n")

    # starts a new game 
    if not loaded:
        while True:
            try:
                player_age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Error: Invalid number")

        # game is rated K12
        if player_age < 12:
            print("Underage, exiting.")
            exit()

        player = game.Player(player_name, player_age)
        lake = game.Lake()

        with open("intro.txt", "r") as intro:
            print(intro.read())
        with open("instructions.txt", "r") as instructions:
            print(instructions.read())
            
        sleep(2)
    
    while player.day <= 7:
        print(f"\n--- Day {player.day} ---")

        while True:
            try:
                action = int(input("--- What will you do for the day? ---\n\t[1] Go fish\n\t[2] Sleep (skip 1 day)\n\t[3] List caught fish\n\t[4] Save data\n\t[5] Quit\n\tInput: "))
                break
            except ValueError:
                print("Error: Invalid number")

        match action:
            case 1:
                game.catch_fish(player, lake)
                player.day += 1
                sleep(2)
            case 2:
                print("Sleeping...")
                player.day += 1
                sleep(3)
            case 3:
                player.list_fish()
                sleep(2)
            case 4:
                print("Saving...")
                sleep(2)
                print("Saved!")
                game.save_game(player, lake)
            case 5:
                print("Quitting..")
                break
            case _:
                print("Invalid action")
                sleep(2)

    # add a check, so whatever is inside doesnt trigger if the player quits instead of completing the week
    if player.day > 7:
        print(f"\n\t--- End of Week Results ---")

        # results of the player's behaviour
        print(f"\n\t{game.calculate_lake_health(player)}\n")

        net_profit, total_worth, total_fines = game.calculate_bucket_worth(player)
        print(f"\tTotal Bucket Worth -- {total_worth:.2f}€\n\tTotal Fines -- {total_fines:.2f}€\n\tNet-Profit -- {net_profit:.2f}€")

main()


