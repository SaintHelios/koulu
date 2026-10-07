import json
import random
from time import sleep
from .player import Player
from .fish import Fish
from .lake import Lake

def catch_fish(player, lake):
   print("You cast your line into the silly waters...")
   sleep(1)
    
   # random wait time between 1 and 3 seconds
   wait_time = random.randint(1, 3)
   for _ in range(wait_time):
       print("... *bobber floats* ...")
       sleep(1)
        
   print("\nSPLASH! YOU GOT A BITE!")
   sleep(1)


   # pop returns and removes a fish from the lake
   catch = lake.fishes.pop(0)
   print(f"Caught a {catch.rarity} {catch.name} ~ {catch.weight}kg")

   while True:
       try:
           choice = int(input("--- What will you do? ---\n\t[1] Keep fish\n\t[2] Release fish\n\tInput: "))
           break
       except ValueError:
           print("Error: Enter a number.")

   if choice == 1:
       player.bucket.append(catch)
       print("Fish added to the bucket")
   else:
       print("Fish released")
        # didn't append the fish back into the lake
        # it'd be boring if the player would catch it twice

def calculate_lake_health(player):
    total = 0
    for fish in player.bucket:
        if fish.size == "small":
            total += 1
    if total == 0:
        return "Pristine! You spared the youth. The local game warden sheds a single tear of joy. Silly Lake's future is secure."
    elif total < 3: 
        return "A bit greedy, huh? You kept a few little ones. The lake will recover, but the local seagulls are judging you heavily."
    else:
        return "ECOLOGICAL WAR CRIMES! You vacuumed up the babies. You leave behind a barren puddle of despair and a very angry fishing inspector."    

def save_game(player, lake):

    # appends a dictionary of the fish into the list
    # __dict__ at work
    bucket_data = []
    for fish in player.bucket:
        bucket_data.append(fish.__dict__)
    
    lake_data = []
    for fish in lake.fishes:
        lake_data.append(fish.__dict__)

    # dictionary of the two lists above, which hold dictionaries
    # python programming in a nutshell
    save_data = {
        "name": player.name,
        "age": player.age,
        "day": player.day,
        "bucket": bucket_data,
        "lake_fishes": lake_data
    }

    # using the player's name, making saves unique
    filename = f"{player.name}_save.json"
    with open(filename, "w", ) as file:
        json.dump(save_data, file)

def load_data(player_name):
    filename = f"{player_name}_save.json"
    
    # try keyword, so the game doesn't crash if: \\FileNotFoundError\\
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        
        # creating a new object by appending dictionary keys as arguments
        player = Player(data["name"], data["age"])
        player.day = data["day"]
        
        # same thing as the above
        # this time iterating through dictionaries inside the list
        for fish in data["bucket"]:
            player.bucket.append(Fish(fish["name"], fish["weight"], fish["value"], fish["rarity"]))
            
        # same thing as the past 2 for loops
        lake = Lake()
        lake.fishes = []
        for f in data["lake_fishes"]:
            lake.fishes.append(Fish(f["name"], f["weight"], f["value"], f["rarity"]))
            
        # returns objects 
        return player, lake
        
    except FileNotFoundError:
        return None, None

def calculate_bucket_worth(player):
    worth = 0
    fines = 0

    for fish in player.bucket:
        worth += fish.value
        
        if fish.size == "small":
            fines += 50
    net_profit = worth - fines

    return net_profit, worth, fines
    

