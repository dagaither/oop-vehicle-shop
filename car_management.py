import time

class CarManager:
    all_cars = []
    total_cars = 0
    terminal = None

    def __init__(self, make, model, year, mileage, services=[]):
        self._id = CarManager.total_cars
        CarManager.total_cars += 1
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services
        CarManager.all_cars.append(self)

    def __repr__(self):
        return f"ID: {self._id} | {self._year} {self._make} {self._model} | Mileage: {self._mileage} | Services: {self._services}"

    def details(self):
        return f"ID {self._id}: {self._year} {self._make} {self._model}"
    
    @classmethod
    def add_car(cls, make, model, year, mileage, services=[]):
        cls(make, model, year, mileage, services)
        cls.terminal.clear()
        print("\nCar added successfully!")
        time.sleep(2)

    @classmethod
    def print_menu(cls):
        cls.terminal.clear()
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

    @classmethod
    def get_choice(cls):
        user_choice = input("Make a selection (1-7): ")
        try:
            user_choice = int(user_choice)
            if user_choice in range(1, 8):
                return user_choice
            else:
                cls.terminal.clear()
                print("\nInvalid selection!")
                time.sleep(1)
        except ValueError:
            cls.terminal.clear()
            print("\nInvalid selection, must be a number!")
            time.sleep(2)

    @classmethod
    def get_car_id(cls):
        while True:
            car_id = input("\nEnter car ID: ")
            try:
                car_id = int(car_id)
                if car_id < len(cls.all_cars):
                    return car_id
                else:
                    cls.terminal.clear()
                    print("\nInvalid car ID!")
                    time.sleep(1)
            except ValueError:
                cls.terminal.clear()
                print("\nInvalid selection, must be a number!")
                time.sleep(2)

    @classmethod
    def add_service(cls):
        car_id = cls.get_car_id()
        service = input("\nEnter the service to add to the vehicle's record: ")
        cls.all_cars[car_id]._services.append(service)
        cls.terminal.clear()
        print("\nService added!")
        time.sleep(2)

    @classmethod
    def update_mileage(cls):
        car_id = cls.get_car_id()
        mileage = input("\nEnter updated mileage: ")
        try:
            if int(mileage) > int(cls.all_cars[car_id]._mileage):
                cls.all_cars[car_id]._mileage = mileage
                cls.terminal.clear()
                print("\nMileage updated!")
                time.sleep(2)
                    
            else:
                cls.terminal.clear()
                print("Can't roll back an odometer!")
                time.sleep(2)
        except ValueError:
            cls.terminal.clear()
            print("Mileage must be an integer.")
            time.sleep(2)

    @classmethod
    def main(cls):
        while True:
            cls.print_menu()
            choice = cls.get_choice()

            if choice == 1:
                make = input("Enter make: ")
                model = input("Enter model: ")
                year = input("Enter year: ")
                mileage = input("Enter vehicle mileage: ")
                cls.add_car(make, model, year, mileage)

            elif choice == 2:
                cls.view_cars()

            elif choice == 3:
                cls.view_num_cars()

            elif choice == 4:
                cls.view_car_details()

            elif choice == 5:
                cls.add_service()

            elif choice == 6:
                cls.update_mileage()

            elif choice == 7:
                return

    @classmethod
    def view_cars(cls):
        cls.terminal.clear()
        print("\n--- Car Inventory ---")
        for car in cls.all_cars:
            print(car.details())
        cls.terminal.pause("\nPress Enter to return to the main menu...")

    @classmethod
    def view_num_cars(cls):
        cls.terminal.clear()
        print("\n--- Cars Total ---")
        if len(cls.all_cars) == 1:
            print(f"\nThere is currently 1 car in inventory.")
        else:
            print(f"\nThere are currently {len(cls.all_cars)} cars in inventory.")
        cls.terminal.pause("\nPress Enter to return to the main menu...")

    @classmethod
    def view_car_details(cls):
        car_id = cls.get_car_id()
        cls.terminal.clear()
        print("\n--- Car Details ---")
        print(cls.all_cars[car_id])
        cls.terminal.pause("\nPress Enter to return to the main menu...")

    @staticmethod
    def mileage_str_to_int(mileage):
        stripped_mileage = ""
        for i in mileage:
            if i.isnum():
                stripped_mileage += i
        return int(stripped_mileage)

class Terminal:
    @staticmethod
    def clear():
        print("\033c", end="")

    @staticmethod
    def pause(message):
        input(message)

# Setting the terminal for CarManager
CarManager.terminal = Terminal()

# Running the main loop
CarManager.main()
