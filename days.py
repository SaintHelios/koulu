days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day_number = int(input("Enter the day number (1-7): "))
day = days_of_the_week[day_number-1]
print(f"Day number {day_number} is {day}.")

