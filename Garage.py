import time


class Car:
    def __init__(self, make, model, year, color, zero_to_sixty, max_speed, car_type, ev_classification):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.zero_to_sixty = zero_to_sixty
        self.max_speed = max_speed
        self.car_type = car_type  # Sports, Luxury, Sedan, SUV, Truck
        self.ev_classification = ev_classification  # EV (Electric Vehicle) classification
        self.checkedOut = False


garage = []


def add_cars_to_garage():
    # Adding Sedans
    add_car("Toyota", "Corolla", "2022", "Blue", "9.2 sec", "200 km/h", "Sedan", "Non-EV")
    add_car("Honda", "Civic", "2021", "Red", "8.7 sec", "190 km/h", "Sedan", "Non-EV")
    add_car("Nissan", "Leaf", "2023", "Silver", "7.9 sec", "150 km/h", "Sedan", "EV")

    # Adding SUVs
    add_car("Ford", "F-150", "2022", "Gray", "6.9 sec", "180 km/h", "SUV", "Non-EV")
    add_car("Tesla", "Model Y", "2023", "White", "4.8 sec", "250 km/h", "SUV", "EV")

    # Adding Sports cars
    add_car("Lamborghini", "Huracan", "2021", "Orange", "2.9 sec", "325 km/h", "Sports", "Non-EV")
    add_car("Porsche", "911 Carrera", "2023", "Yellow", "3.4 sec", "320 km/h", "Sports", "Non-EV")

    # Adding Luxury cars
    add_car("Mercedes-Benz", "C-Class", "2023", "Gray", "5.9 sec", "250 km/h", "Luxury", "Non-EV")
    add_car("BMW", "7 Series", "2022", "Black", "5.5 sec", "240 km/h", "Luxury", "Non-EV")

    # Additional cars of various types
    add_car("Toyota", "Camry", "2021", "Black", "8.5 sec", "210 km/h", "Sedan", "Non-EV")
    add_car("Toyota", "Prius", "2023", "Green", "8.5 sec", "185 km/h", "Sedan", "EV")
    add_car("Nissan", "Altima", "2022", "White", "8.3 sec", "195 km/h", "Sedan", "EV")
    add_car("Ford", "Ranger", "2023", "Blue", "7.5 sec", "175 km/h", "Truck", "Non-EV")
    add_car("Tesla", "Model 3", "2022", "Black", "5.3 sec", "233 km/h", "Sedan", "EV")
    add_car("Chevrolet", "Cruze", "2022", "Silver", "9.0 sec", "185 km/h", "Sedan", "Non-EV")
    add_car("Chevrolet", "Trax", "2023", "Blue", "8.5 sec", "195 km/h", "SUV", "Non-EV")
    add_car("Chevrolet", "Equinox", "2022", "Red", "7.7 sec", "205 km/h", "SUV", "Non-EV")
    
    # Adding more cars of various types and brands
    add_car("Toyota", "Supra", "2023", "Yellow", "4.0 sec", "280 km/h", "Sports", "Non-EV")
    add_car("Toyota", "Camry", "2023", "Red", "7.2 sec", "215 km/h", "Sedan", "Non-EV")
    add_car("Honda", "Accord", "2022", "White", "7.8 sec", "195 km/h", "Sedan", "Non-EV")
    add_car("Ford", "Mustang", "2023", "Red", "4.5 sec", "310 km/h", "Sports", "Non-EV")
    add_car("Ford", "Explorer", "2022", "Black", "6.2 sec", "180 km/h", "SUV", "Non-EV")
    add_car("Chevrolet", "Camaro", "2022", "Blue", "5.0 sec", "290 km/h", "Sports", "Non-EV")
    add_car("Chevrolet", "Tahoe", "2023", "White", "6.5 sec", "230 km/h", "SUV", "Non-EV")
    add_car("Nissan", "Maxima", "2023", "Gray", "6.9 sec", "200 km/h", "Sedan", "Non-EV")
    add_car("Nissan", "Rogue", "2022", "Silver", "8.1 sec", "190 km/h", "SUV", "Non-EV")
    add_car("Tesla", "Model S", "2023", "Midnight Blue", "3.5 sec", "260 km/h", "Sedan", "EV")
    add_car("Tesla", "Model X", "2023", "Red", "4.2 sec", "240 km/h", "SUV", "EV")
    add_car("Mercedes-Benz", "E-Class", "2022", "Black", "5.7 sec", "240 km/h", "Luxury", "Non-EV")
    add_car("Mercedes-Benz", "S-Class", "2023", "White", "4.4 sec", "250 km/h", "Luxury", "Non-EV")
    add_car("BMW", "5 Series", "2022", "Blue", "5.1 sec", "230 km/h", "Luxury", "Non-EV")
    add_car("BMW", "X5", "2023", "Black", "5.3 sec", "240 km/h", "SUV", "Non-EV")
    add_car("Lamborghini", "Aventador", "2021", "Yellow", "2.8 sec", "350 km/h", "Sports", "Non-EV")
    add_car("Lamborghini", "Urus", "2022", "Blue", "3.6 sec", "305 km/h", "SUV", "Non-EV")
    add_car("Porsche", "Taycan Turbo", "2023", "White", "3.0 sec", "270 km/h", "Sports", "EV")
    add_car("Porsche", "Cayenne", "2022", "Black", "4.9 sec", "265 km/h", "SUV", "Non-EV")


def add_car(make, model, year, color, zero_to_sixty, max_speed, car_type, ev_classification):
    car = Car(make, model, year, color, zero_to_sixty, max_speed, car_type, ev_classification)
    garage.append(car)


def display_cars():
    for car in garage:
        time.sleep(2)
        print("\nMake:", car.make)
        print("Model:", car.model)
        print("Year:", car.year)
        print("Color:", car.color)
        print("0-60 Time:", car.zero_to_sixty)
        print("Max Speed:", car.max_speed)
        print("Car Type:", car.car_type)
        print("EV Classification:", car.ev_classification)
        print("Checked out:", car.checkedOut)
        print("")


def find_car(make, model, color):
    for car in garage:
        if (
            make.lower() == car.make.lower()
            and model.lower() == car.model.lower()
            and color.lower() == car.color.lower()
        ):
            print("\nGood news! Your car was found.")
            print("")
            return car
    print("\nSorry, we couldn't find the car you were looking for.")
    return None


def remove_car(make, model, color):
    for car in garage:
        if (
            make.lower() == car.make.lower()
            and model.lower() == car.model.lower()
            and color.lower() == car.color.lower()
        ):
            garage.remove(car)
            print("\nYour car was removed from the garage.")
            return
    print("\nSorry, we couldn't find the car you were looking for.")


def check_out_car(make, model, color):
    for car in garage:
        if (
            make.lower() == car.make.lower()
            and model.lower() == car.model.lower()
            and color.lower() == car.color.lower()
        ):
            if car.checkedOut:
                print("\nSorry, that car is already checked out.")
            else:
                car.checkedOut = True
                print("\nYou have checked out the", car.color, car.make, car.model)
            return
    print("\nSorry, we couldn't find the car you were looking for.")


def check_in_car(make, model, color):
    for car in garage:
        if (
            make.lower() == car.make.lower()
            and model.lower() == car.model.lower()
            and color.lower() == car.color.lower()
        ):
            if not car.checkedOut:
                print("\nSorry, that car is already checked in.")
            else:
                car.checkedOut = False
                print("\nYou have checked in the", car.color, car.make, car.model)
            return
    print("\nSorry, we couldn't find the car you were looking for.")


def get_cars_by_make(make):
    cars_by_make = []
    for car in garage:
        if car.make.lower() == make.lower():
            cars_by_make.append(car)
    if cars_by_make:
        print(f"\nThese are the cars by {make} that we have in our garage:")
        for car in cars_by_make:
            print(f"{car.color} {car.model} ({car.year})")
        print("")
    else:
        print(f"\nNo cars found by {make}.")


def get_cars_by_type(car_type):
    cars_by_type = []
    for car in garage:
        if car.car_type.lower() == car_type.lower():
            cars_by_type.append(car)
    if cars_by_type:
        print(f"\nThese are the cars of type {car_type} that we have in our garage:")
        for car in cars_by_type:
            print(f"{car.color} {car.make} {car.model} ({car.year})")
        print("")
    else:
        print(f"\nNo cars found of type {car_type}.")


def get_cars_by_ev_class(ev_classification):
    cars_by_ev_class = []
    for car in garage:
        if car.ev_classification.lower() == ev_classification.lower():
            cars_by_ev_class.append(car)
    if cars_by_ev_class:
        print(f"\nThese are the cars of EV class {ev_classification} that we have in our garage:")
        for car in cars_by_ev_class:
            print(f"{car.color} {car.make} {car.model} ({car.year})")
        print("")
    else:
        print(f"\nNo cars found in EV class {ev_classification}.")


def add_car_from_prompt():
    make = input("\nEnter the make of the car: ")
    model = input("Enter the model of the car: ")
    year = input("Enter the year the car was manufactured: ")
    color = input("Enter the color of the car: ")
    zero_to_sixty = input("Enter the 0-60 time of the car: ")
    max_speed = input("Enter the max speed of the car: ")
    car_type = input("Enter the type of the car (Sports, Luxury, Sedan, SUV, Truck): ")
    ev_classification = input("Enter the EV classification of the car (EV or Non-EV): ")
    add_car(make, model, year, color, zero_to_sixty, max_speed, car_type, ev_classification)


def find_car_from_prompt():
    make = input("\nEnter the make of the car you are looking for: ")
    model = input("Enter the model of the car you are looking for: ")
    color = input("Enter the color of the car you are looking for: ")
    find_car(make, model, color)


def get_make_from_prompt():
    make = input("\nEnter the make of the cars you want to find: ")
    get_cars_by_make(make)


def get_type_from_prompt():
    car_type = input("\nEnter the type of car you want to find (Sports, Luxury, Sedan, SUV, Truck): ")
    get_cars_by_type(car_type)


def get_ev_class_from_prompt():
    ev_classification = input("\nEnter the EV classification you want to find (EV or Non-EV): ")
    get_cars_by_ev_class(ev_classification)


def display_menu():
    print("Welcome to the Garage Management System!")
    print("1. Add a car")
    print("2. Find a car")
    print("3. Get cars by brand")
    print("4. Display all cars")
    print("5. Does nothing.")
    print("6. Remove a car")
    print("7. Check out a car")
    print("8. Check in a car")
    print("9. Exit")
    print("10. Add example cars.")
    print("11. Get cars by type")
    print("12. Get cars by EV class")


def handle_input(input_choice):
    if input_choice == "1":
        add_car_from_prompt()
    elif input_choice == "2":
        find_car_from_prompt()
    elif input_choice == "3":
        get_make_from_prompt()
    elif input_choice == "4":
        display_cars()
    elif input_choice == "5":
        time.sleep(3)
        print("\nYou waited...")
        time.sleep(4)
        print(".......")
        time.sleep(5)
        print("But nothing happened....")
        time.sleep(2)
        return True
    elif input_choice == "6":
        make = input("\nEnter the brand of the car you want to remove: ")
        model = input("Enter the model of the car you want to remove: ")
        color = input("Enter the color of the car you want to remove: ")
        remove_car(make, model, color)
    elif input_choice == "7":
        make = input("\nEnter the brand of the car you want to check out: ")
        model = input("Enter the model of the car you want to check out: ")
        color = input("Enter the color of the car you want to check out: ")
        check_out_car(make, model, color)
    elif input_choice == "8":
        make = input("\nEnter the brand of the car you want to check in: ")
        model = input("Enter the model of the car you want to check in: ")
        color = input("Enter the color of the car you want to check in: ")
        check_in_car(make, model, color)
    elif input_choice == "9":
        print("\nThank you for using the Garage Management System.")
        return True
    elif input_choice == "10":
        add_cars_to_garage()
    elif input_choice == "11":
        get_type_from_prompt()
    elif input_choice == "12":
        get_ev_class_from_prompt()
    else:
        print("\nInvalid input. Please try again.")


def start():
    while True:
        display_menu()
        input_choice = input("\nEnter your choice: ")
        if handle_input(input_choice):
            break


if __name__ == "__main__":
    add_cars_to_garage()
    start()
