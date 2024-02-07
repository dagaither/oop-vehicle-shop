import time

# CarManager class
class CarManager:
    all_cars = []
    total_cars = 0

    def __init__(self, make, model, year, mileage, servivces=[]):
        self._id = CarManager.total_cars
        CarManager.total_cars += 1
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = servivces
        CarManager.all_cars.append(self)

    def __repr__(self):
        return f"ID: {self._id} | {self._year} {self._make} {self._model} | Mileage: {self._mileage} | Services: {self._services}"

    def details(self):
        return f"ID {self._id}: {self._year} {self._make} {self._model}"
    
    @classmethod
    def add_car(cls, make, model, year, mileage, services=[]):
        cls(make, model, year, mileage, services)
        print("\nCar added successfully!")
        time.sleep(1)
        input("\nPress Enter to return to the main menu...")


# Print main menu
def print_menu():
    print(
    """
    --- WELCOME ---
    1. Add a car
    2. View all cars
    3. View total number of cars
    4. See a car's details
    5. Service a car
    6. Update mileage
    7. Quit
    """)


# Allow user to make a menu selection
def get_choice():
    user_choice = input("Make a selection (1-7): ")
    try:
        user_choice = int(user_choice)
        if user_choice in range(1, 8):
            return user_choice
        else:
            print("\nInvalid selection!")
            time.sleep(1)
    except ValueError:
        print("\nInvalid selection, must be a number!")
        time.sleep(2)


# Get car ID
def get_car_id():
    while True:
        car_id = input("\nEnter car ID: ")
        try:
            car_id = int(car_id)
            if car_id < len(CarManager.all_cars):
                return car_id
            else:
                print("\nInvalid car ID!")
                time.sleep(1)
        except ValueError:
            print("\nInvalid selection, must be a number!")
            time.sleep(2)


# Add new car
def add_car():
    print("\n --- Add Car ---")
    make = input("Enter make: ")
    model = input("Enter model: ")
    year = input("Enter year: ")
    mileage = input("Enter vehicle mileage: ")
    CarManager.add_car(make, model, year, mileage)


# View car inventory
def view_cars():
    print("\n--- Car Inventory ---")
    for car in CarManager.all_cars:
        print(car.details())
    input("\nPress Enter to return to the main menu...")


# Get total number of car
def view_num_cars():
    print("\n--- Cars Total ---")
    print(f"\nThere are currently {len(CarManager.all_cars)} cars in inventory.")
    input("\nPress Enter to return to the main menu...")


# View specific car details
def view_car_details():
    car_id = get_car_id()
    print("\n--- Car Details ---")
    print(CarManager.all_cars[car_id])
    input("\nPress Enter to return to the main menu...")


#  Add service record
def add_service():
    car_id = get_car_id()
    service = input("\nEnter the service to add to the vehicle's record: ")
    CarManager.all_cars[car_id]._services.append(service)
    print("\nService added!")
    time.sleep(2)


#  Update mileage
def update_mileage():
    car_id = get_car_id()
    mileage = input("\nEnter updated mileage: ")
    CarManager.all_cars[car_id]._mileage = mileage
    print("\nMileage updated!")
    time.sleep(2)

  
#  Main menu
def main():
    while True:
        print_menu()
        choice = get_choice()
        
        if choice == 1:
            add_car()

        elif choice == 2:
            view_cars()

        elif choice == 3:
            view_num_cars()

        elif choice == 4:
            view_car_details()

        elif choice == 5:
            add_service()

        elif choice == 6:
            update_mileage()

        elif choice == 7:
            return

    

car1 = CarManager("Toyota", "Camry", "2024", "100")
car2 = CarManager("Nissan", "Pathfinder", "2019", "29,500")
car3 = CarManager("Pontiac", "Trans Am", "1998", "210,000")

main()