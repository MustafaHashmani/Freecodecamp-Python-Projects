import copy
import random


class Hat:
    def __init__(self, **kwargs):
        # make a list of all balls
        contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                contents.append(key)
        self.contents = contents

    def draw(self, num_balls_draw):
        # make a list of all balls drawn randomly without replacement
        if num_balls_draw <= len(self.contents):
            list_of_balls = []
            for _ in range(num_balls_draw):
                ball = random.choice(self.contents)
                list_of_balls.append(random.choice(self.contents))
                self.contents.remove(ball)
        return list_of_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        balls_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors = hat_copy.draw(num_balls_drawn)

        # if balls drawn are in expected_balls, remove them
        for color in colors:
            if color in balls_copy:
                balls_copy[color] -= 1

        if all(x <= 0 for x in balls_copy.values()):
            count += 1

    return count / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000,
)
