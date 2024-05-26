import unittest
from functions import greedy_algorithm, dynamic_programming


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.foods = {
            'піца': {'cost': 50, 'calories': 300},
            'гамбургер': {'cost': 40, 'calories': 250},
            'хот-дог': {'cost': 30, 'calories': 200}
        }

    def test_greedy_foods(self):
        result, total_price, total_calories = greedy_algorithm(self.foods, 100)
        self.assertEqual(total_price, 70)
        self.assertEqual(total_calories, 450)
        self.assertIn('гамбургер', result)
        self.assertIn('хот-дог', result)

    def test_dynamic_programming(self):
        result, total_price, total_calories = dynamic_programming(
            self.foods, 100)
        self.assertEqual(total_price, 90)
        self.assertEqual(total_calories, 550)
        self.assertIn('піца', result)
        self.assertIn('гамбургер', result)


if __name__ == '__main__':
    unittest.main()
