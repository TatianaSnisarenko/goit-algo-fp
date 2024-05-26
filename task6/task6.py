
from functions import greedy_algorithm, dynamic_programming


if __name__ == '__main__':
    foods = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = 100

    print("Greedy algorithm:")
    food_names, total_price, total_calories = greedy_algorithm(foods, budget)
    print(f"Total price: {total_price}")
    print(f"Total calories: {total_calories}")
    print(f"Choosen food: {food_names}")

    food_names, total_price, total_calories = dynamic_programming(
        foods, budget)

    print(f"Total price: {total_price}")
    print(f"Total calories: {total_calories}")
    print(f"Choosen food: {food_names}")
