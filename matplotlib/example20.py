# Jupyter Notebook
#
# Dvacátý demonstrační příklad:
# - sloupcový graf se dvěma skupinami sloupců
# - přidání popisů os, titulku aj.

import numpy as np
import matplotlib.pyplot as plt

# první pole hodnot
vals1 = [10, 15, 20, 12, 14, 8]

# druhé pole hodnot
vals2 = [19, 18,  6, 11,  6, 14]

# počet prvků
N = len(vals1)

# indexy prvků
indexes = np.arange(N)

# šířka sloupců
width = 0.30

# titulek grafu
plt.title("Sloupcový graf se dvěma skupinami sloupců")

# sloupcový graf se dvěma skupinami sloupců
plt.bar(indexes, vals1, width, color='gray', edgecolor='black', label='Pobočka 1')

# posunuté sloupce
plt.bar(indexes+width, vals2, width, color='red', edgecolor='black',
        label='Pobočka 2')

# povolení zobrazení mřížky
plt.grid(True)

# popisek vodorovné osy
plt.xlabel("Měsíc")

# popisek svislé osy
plt.ylabel("Zisk pobočky")

# přidání legendy
plt.legend(loc="upper right")

# popisky
plt.xticks([0, 1, 2, 3, 4, 5], ['Leden', 'Únor', 'Březen', 'Duben', 'Květen', 'Červen'], rotation=20)

# změna pozic jednotlivých prvků grafu
plt.tight_layout()

# zobrazení grafu
plt.show()
