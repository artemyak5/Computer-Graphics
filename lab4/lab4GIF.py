import matplotlib.pyplot as plt
import numpy as np
import imageio
from tempfile import NamedTemporaryFile

def generate_fractal(rules, iterations):
    x, y = [0], [0]
    for _ in range(iterations):
        rule = np.random.choice(rules, p=[r.get('p', 1/len(rules)) for r in rules])
        new_x = rule.get('a', rule.get('r', 1) * np.cos(rule.get('theta', 0))) * x[-1] + \
                rule.get('b', -rule.get('s', 1) * np.sin(rule.get('phi', 0))) * y[-1] + rule.get('e', 0)
        new_y = rule.get('c', rule.get('r', 1) * np.sin(rule.get('theta', 0))) * x[-1] + \
                rule.get('d', rule.get('s', 1) * np.cos(rule.get('phi', 0))) * y[-1] + rule.get('f', 0)
        x.append(new_x)
        y.append(new_y)
    return x, y

def display_fractal(rules, iterations, delay, pixels, filename='fractal.gif'):
    x, y = generate_fractal(rules, iterations)
    plt.figure()
    frames = []
    for i in range(0, iterations + 1, pixels):
        plt.plot(x[:i], y[:i], '*', color='green', markersize=0.5)
        plt.title('Fractal Generation')
        plt.axis('off')

        with NamedTemporaryFile(delete=True, suffix='.png') as tmpfile:
            plt.savefig(tmpfile.name)
            frames.append(imageio.imread(tmpfile.name))

        plt.pause(delay)

    imageio.mimsave(filename, frames, duration=delay)
    plt.close()

rules = [
    {'a': 0.1400, 'b': 0.0100, 'c': 0.0000, 'd': 0.5100, 'e': -0.0800, 'f': -1.3100},
    {'a': 0.4300, 'b': 0.5200, 'c': -0.4500, 'd': 0.5000, 'e': 1.4900, 'f': -0.7500},
    {'a': 0.4500, 'b': -0.4900, 'c': 0.4700, 'd': 0.4700, 'e': -1.6200, 'f': -0.7400},
    {'a': 0.4900, 'b': 0.0000, 'c': 0.0000, 'd': 0.5100, 'e': 0.0200, 'f': 1.6200}
]

# Running the display function
display_fractal(rules, iterations=10000, delay=0.0001, pixels=500, filename='fractal_animation.gif')
