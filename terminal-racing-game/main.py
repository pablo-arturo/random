import os
import sys
import random
import time

road_length = 15
selected_car = None

cars_data = [
    {"position": road_length - 1, "symbol": "🚗", "number": 50},
    {"position": road_length - 1, "symbol": "🚙", "number": 95},
    {"position": road_length - 1, "symbol": "🚙", "number": 55},
    {"position": road_length - 1, "symbol": "🚗", "number": 99},
    {"position": road_length - 1, "symbol": "🚙", "number": 76},
]


def choose_a_car():
    global selected_car

    print("CHOOSE YOUR CAR\n")
    for i, car in enumerate(cars_data):
        print(f"({i+1}) {car["symbol"]} Number #{car["number"]}")

    input_value = input(
        f"\nWrite the number of the option from 1 to {len(cars_data)}: "
    )
    while (
        not input_value.isdigit()
        or int(input_value) < 1
        or int(input_value) > len(cars_data)
    ):
        print("\nInvalid option, please try again")
        input_value = input(
            f"Write the number of the option from 1 to {len(cars_data)}: "
        )

    selected_car = int(input_value) - 1


def run_race():
    clear_console()
    for car in cars_data:
        print("- " * car["position"] + car["symbol"] + "  " + car_label(car))

    print("\n3")
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print("GOO!! 🏁🏁")
    time.sleep(0.5)
    while all(car["position"] > 0 for car in cars_data):
        clear_console()
        for car in cars_data:
            car["position"] = max(car["position"] - random.randint(1, 3), 0)
            print(
                "- " * car["position"]
                + car["symbol"]
                + "💨"
                + "- " * (road_length - 1 - car["position"])
                + car_label(car)
            )

        time.sleep(0.5)


def car_label(car):
    if car["number"] == cars_data[selected_car]["number"]:
        return f"#{car["number"]} YOUR CAR!"
    return f"#{car["number"]}"


def clear_console():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")


def main():
    clear_console()
    print("Terminal Racing Game 🏁")
    choose_a_car()
    run_race()

    winning_cars = [car for car in cars_data if car["position"] == 0]
    while len(winning_cars) > 1:
        print("\nTHERE WAS A TIE, THE RACE WILL BE REPEATED")
        input("Press enter to continue ")
        for car in cars_data:
            car["position"] = road_length - 1

        run_race()
        winning_cars = [car for car in cars_data if car["position"] == 0]

    if cars_data[selected_car]["number"] == winning_cars[0]["number"]:
        print("\nYOU WON!!! :)")
    else:
        print(f"\nYOU LOST :(")
        print(f"The winner is car number {winning_cars[0]["number"]}")


main()
