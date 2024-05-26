def calorie_to_price_ratio(food_properties):
    return food_properties["calories"] / food_properties["cost"]


def greedy_algorithm(foods, budget):
    sorted_foods = sorted(
        foods.items(), key=lambda x: calorie_to_price_ratio(x[1]), reverse=True)
    total_price = 0
    total_calories = 0
    result = []
    for food_name, food_properties in sorted_foods:
        cost = food_properties['cost']
        calories = food_properties['calories']
        if cost <= budget:
            budget -= cost
            total_price += cost
            total_calories += calories
            result.append(food_name)
    return result, total_price, total_calories


def dynamic_programming(items, budget):
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    for i, (_, properties) in enumerate(items.items(), start=1):
        cost = properties['cost']
        calories = properties['calories']
        for j in range(1, budget + 1):
            if cost > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + calories)

    selected_items = []
    i, j = len(items), budget
    total_price = 0
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            selected_items.append(list(items.keys())[i-1])
            total_price += items[list(items.keys())[i-1]]['cost']
            j -= items[list(items.keys())[i-1]]['cost']
        i -= 1

    total_calories = dp[len(items)][budget]
    return selected_items, total_price, total_calories
