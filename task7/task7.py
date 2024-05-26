import pandas as pd
import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Ініціалізуємо словник для підрахунку кількості випадків для кожної суми
    sums_count = {i: 0 for i in range(2, 13)}

    # Симулюємо кидки кубиків
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_sum = roll1 + roll2
        sums_count[roll_sum] += 1

    # Обчислюємо ймовірності для кожної суми
    probabilities = {sum_: count / num_rolls for sum_,
                     count in sums_count.items()}
    return probabilities


def probabilities_to_dataframe(probabilities, analytic_result):
    in_percetages = {sum_: round(prob * 100, 2)
                     for sum_, prob in probabilities.items()}
    df = pd.DataFrame(list(in_percetages.items()),
                      columns=['Сума', 'Ймовірність'])

    df['Аналітичні результати'] = df['Сума'].map(analytic_result)
    df['Похибка'] = df['Ймовірність'] - df['Аналітичні результати']
    return df


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color='skyblue', edgecolor='black')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум кидків двох кубиків')
    plt.xticks(sums)
    plt.show()


if __name__ == "__main__":
    num_rolls = 1000000  # Кількість кидків кубиків
    probabilities = simulate_dice_rolls(num_rolls)
    plot_probabilities(probabilities)

    analytic_result = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
                       7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}
df = probabilities_to_dataframe(probabilities, analytic_result)
print(df.to_string(index=False))
