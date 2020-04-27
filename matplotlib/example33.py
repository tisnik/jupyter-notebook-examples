# Jupyter Notebook
#
# Třicátý třetí demonstrační příklad:
# - Animace grafu kontur

# import všech potřebných knihoven - Numpy a Matplotlibu
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


from matplotlib import animation, rc
from IPython.display import HTML

# příprava grafu
fig = plt.figure()

delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R1 = np.sqrt(X*X+Y*Y)

# vzdálenost od bodu [3,3]
R2 = np.sqrt((X-3)*(X-3)+(Y-3)*(Y-3))

# funkce zavolaná pro vytvoření každého snímku
def animate(i):
    # výpočet funkce, kterou použijeme při vykreslování grafu
    Z = np.sin(R1)-np.cos(R2+2*np.pi*i/100)

    # povolení zobrazení mřížky
    plt.grid(True)

    # vytvoření grafu s konturami funkce z=f(x,y)
    cnt = plt.contour(X, Y, Z)

    return cnt

anim = animation.FuncAnimation(fig, animate,
                               frames=100, interval=20, blit=False)

HTML(anim.to_html5_video())
