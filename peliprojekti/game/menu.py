def catch_fish(player, lake):
    # poistaa kalan listalta, jottei sitä napata toista kertaa
   catch = lake.fishes.pop(0)
   print(f"Caught a {catch.name}, {catch.weight}kg = {catch.size}")

   choice = int(input("Action:\n(1): Keep fish\n(2): Release fish\n: "))

   if choice == 1:
       player.bucket.append(catch)
       print("Fish added to the bucket")
   else:
       print("Fish released")
        # didn't append the fish back into the lake
        # it'd be boring if the player would catch it twice

