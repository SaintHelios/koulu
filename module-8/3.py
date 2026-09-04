airports = {}

while True:
    selection = input("\n\t(1) Enter a new airport\n\t(2) Fetch an airport\n\t(3) Quit\n")

    if selection == "1":
        icao = input("Submit ICAO: ")
        airport = input("Submit airport name: ")
        airports.update({icao: airport})
    elif selection == "2":
        icao = input("Submit the airport's ICAO: ")
        print(airports[icao])
    elif selection == "3":
        break

