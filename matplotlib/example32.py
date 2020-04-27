# Jupyter Notebook
#
# Třicátý druhý demonstrační příklad:
# - Jednoduchá animace

# import všech potřebných knihoven - Numpy a Matplotlibu
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from IPython.display import HTML

# příprava grafu
fig, ax = plt.subplots()

ax.set_xlim(( 0, 2*np.pi))
ax.set_ylim((-2, 2))

line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)

# funkce zavolaná při inicializaci animace
def init():
    line.set_data([], [])
    line2.set_data([], [])
    return (line,line2,)

# funkce zavolaná pro vytvoření každého snímku
def animate(i):
    # hodnoty na x-ové ose
    x = np.linspace(0, 2*np.pi, 100)
    
    # hodnoty na y-ové ose: první funkce
    y1 = np.sin(x + np.pi*i/50)

    # hodnoty na y-ové ose: druhá funkce
    y2 = np.cos(x + np.pi*i/25)

    line.set_data(x, y1)
    line2.set_data(x, y2)
    return (line,line2,)

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)


HTML(anim.to_html5_video())
