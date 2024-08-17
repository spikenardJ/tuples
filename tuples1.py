# Question 1: Tuple Mastery in Python

# Task 1: Formatting Flight Itineraries

def add_new_itinerary(itinerary):
    traveler_name = input("Enter the name of the traveler: ").title()
    origin = input("Enter the origin of the itinerary: ").title()
    destination = input("Enter the destination of the itinerary: ").title()

    if origin == destination:
        print("Origin and destination cannot be the same.")
        return
    else:
        itinerary.append((traveler_name, origin, destination))
        print("Itinerary added successfully.")


def display_itineraries(itinerary):
    found = False
    for i, trip in enumerate(itinerary):
        print(f"\nItinerary {i + 1}: {trip[0]} - From {trip[1]} to {trip[2]}")
        found = True
    if not found:
        print("No itineraries were found.")

def main():
    itinerary = []
    while True:
        print("\n1. Add a new itinerary")
        print("2. Display all itineraies")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_itinerary(itinerary)
        elif choice == "2":
            display_itineraries(itinerary)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()