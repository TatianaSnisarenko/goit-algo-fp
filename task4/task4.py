
import random
from heap import draw_heap


if __name__ == '__main__':
    data = random.sample(range(1, 101), 15)
    draw_heap(data)
