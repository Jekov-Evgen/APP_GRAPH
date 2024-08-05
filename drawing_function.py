import matplotlib.pyplot as plt
import numpy as np  
  
def plot_function(expression, x_range):
    x = np.linspace(*x_range, 100)
    y = eval(expression)

    fig, ax = plt.subplots()
    ax.set_title("График")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid()

    ax.plot(x, y)
    plt.show()